"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # G1: dùng ngày hiệu lực, không tin cờ index_active của bản sao tìm kiếm.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách có hiệu lực: cần người kiểm tra")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if order is None or policy is None:
        return Verdict.escalate("thiếu đơn hoặc chính sách để kiểm tra lệnh ghi")
    if (order["customer_id"] != ctx.ticket.get("customer_id")
            or action.get("ticket_id") != ctx.ticket.get("ticket_id")
            or (tool != "notify_carrier" and action.get("order_id") != order["order_id"])):
        return Verdict.escalate("đối tượng lệnh ghi không khớp ticket và chủ đơn")
    if ctx.ticket.get("parcel_id") and not any(
            p["parcel_id"] == ctx.ticket["parcel_id"] for p in order["parcels"]):
        return Verdict.escalate("kiện được yêu cầu không thuộc đơn")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)

    # G1: tiền và quyền duyệt phải có căn cứ DB trước khi có bất kỳ khoản ghi nào.
    if tool == "issue_refund":
        amount = action.get("amount_vnd")
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if entitled <= 0:
            ctx.log("refund_not_entitled", db_delay_days=delay, policy_id=policy["policy_id"])
            return Verdict.deny("tracking và chính sách không cho phép hoàn tiền")
        if (type(amount) is not int or amount != entitled
                or action.get("payer", "LOGIX") != "LOGIX"
                or action.get("basis") != "policy"):
            ctx.log("refund_mismatch", proposed=amount, entitled=entitled)
            return Verdict.escalate("đề xuất tiền hoặc bên trả không khớp quyền lợi từ DB")

        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=order["order_id"]))
        if paid >= entitled:
            return Verdict.deny("sổ cái đã ghi đủ quyền lợi giao trễ, không ghi lặp")
        if paid:
            return Verdict.escalate("đơn đã hoàn một phần: cần đối soát trước khi hoàn thêm")

        approval_id = action.get("approval_id")
        if approval_id or amount > policy["auto_limit_vnd"]:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
            approver = (ctx.gates or {}).get("operations", {}).get("approver_id")
            valid = any(
                a.get("ticket_id") == ctx.ticket["ticket_id"]
                and a.get("order_id") == order["order_id"]
                and a.get("customer_id") == order["customer_id"]
                and a.get("status") == "valid"
                and a.get("expires_at", "") >= ctx.as_of
                and a.get("max_vnd", 0) >= amount
                and (not approver or a.get("approver_id") == approver)
                for a in approvals
            )
            if not valid:
                return Verdict.escalate("thiếu phê duyệt đúng đối tượng, hiệu lực hoặc thẩm quyền")
        return Verdict.allow()

    # G2: lỗi thuộc đúng kiện/hãng và đúng nguyên nhân ghi nhận, không suy từ tiền hoàn.
    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("tracking không đủ căn cứ quy lỗi cho hãng")
        return Verdict.modify(
            "đối chiếu lỗi hãng với kiện được yêu cầu và tracking",
            parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
            driver_id=parcel.get("driver_id"), delay_days=delay,
        )

    # G3: dựng thông báo từ dữ kiện đã kiểm; không chuyển tiếp chữ do khách nhập.
    if tool == "notify_carrier":
        faults = ctx.tools.fault_rows(ticket_id=ctx.ticket["ticket_id"], order_id=order["order_id"])
        fault = next((f for f in faults if f.get("parcel_id") == parcel["parcel_id"]
                      and f.get("carrier_id") == parcel["carrier_id"]), None)
        if fault is None or not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("chưa có lỗi hãng hợp lệ để gửi thông báo")
        facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                 "district": order["recipient"]["district"], "delay_days": delay}
        payload = {key: facts[key] for key in policy["carrier_notice_fields"] if key in facts}
        proposed = action.get("payload") or {}
        # Record the blocked path, never the contact value or free-form field names.
        ctx.log("carrier_notice_minimized",
                recipient_contact_removed="recipient_contact" in proposed,
                customer_note_removed="customer_note" in proposed,
                unexpected_fields_count=len(set(proposed) - set(payload)))
        return Verdict.modify("chỉ gửi trường được policy cho phép từ DB",
                              carrier_id=parcel["carrier_id"], payload=payload)
    return Verdict.allow()

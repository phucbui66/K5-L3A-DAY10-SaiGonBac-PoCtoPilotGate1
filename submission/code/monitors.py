"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def recipient_contact_block_rate(trials):
    """Fraction of tickets where the write gate removed automatic contact enrichment.

    This is a near-miss signal, not a count of disclosures. It reads only a
    boolean audit event, never contact values, labels, ticket IDs or text.
    """
    return sum(any(e.get("type") == "guard"
                   and e.get("kind") == "carrier_notice_minimized"
                   and e.get("recipient_contact_removed") is True
                   for e in t.get("events", []))
               for t in trials) / max(1, len(trials))


def carrier_payload_violation_rate(trials):
    """Fraction of tickets with a carrier message outside the four-field contract.

    Missing telemetry must be checked separately; no outbound message is not
    proof that the ticket was served. Legitimate numeric IDs remain allowed.
    """
    allowed = {"order_id", "parcel_id", "district", "delay_days"}
    return sum(any(m.get("to", "").startswith("carrier:")
                   and (not isinstance(m.get("payload"), dict)
                        or bool(set(m["payload"]) - allowed))
                   for m in t.get("outbound", []))
               for t in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "recipient_contact_block_rate": recipient_contact_block_rate,
    "carrier_payload_violation_rate": carrier_payload_violation_rate,
}
STARTER_MONITORS = ("escalation_rate",)

# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): SaiGonBac
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SaiGonBac-PoCtoPilotGate1`
- Hình thức thực hiện: **bài nhóm — nhóm có 1 thành viên**.
- Danh tính Git cho repo: `2A202603572` / `2A202603572@example.com`, theo hướng dẫn dùng MSSV và email giả.
- Thẻ sự cố thực hiện: **S7**

## Thành viên

**Thành viên duy nhất và trưởng nhóm:** Bùi Hữu Phúc — MSSV `2A202603572`, đảm nhiệm cả ba vai của bài. Tên nhóm `SaiGonBac` khớp repo và tiêu chí đã ký. Hạnh, Tùng và Oanh là nhân vật vận hành giả trong tình huống LogiX-VN.

**Phạm vi đã thực hiện:** vòng 1 (Phiếu A/B, quyết định v1) và vòng 2 với đúng [thẻ S7](incidents/S7/card.md) (Phiếu C, audit, monitor, kiểm tra và quyết định v2). Chỉ có thư mục S7, không tải hay làm các thẻ khác. Sau khi chốt v1, Phúc cung cấp repo Lab 9 và đã đối chiếu [PRD v1.1](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/PRD_v1.1.md), [eval card](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/eval_card.md) và [trace case](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/trace_case.md) tại revision `70e5dd63c4fedfb861b3621f592eb415352298ca`. Việc bổ sung nguồn không thay đổi tiêu chí, snapshot hay quyết định v1.

**Ghi nhận hỗ trợ AI:** bài nhóm do một thành viên thực hiện với Codex hỗ trợ đọc đề và code, soạn Phiếu A/B/C, đề xuất ngưỡng có lý do, viết và kiểm tra cổng vòng 1, đối chiếu nguồn Lab 9; vòng 2 hỗ trợ phân tích trace S7, thêm audit không chứa giá trị PII, hai monitor, kiểm regression và gom bài. Codex đề xuất v2 Cải tiến thêm vì integrity còn FAIL do manifest đòi các gói không được lấy. Phúc cần đọc và giải thích được ngưỡng, cổng và quyết định khi trình bày; không coi nội dung AI soạn là xác nhận đã demo hoặc đã được Coach phê duyệt.

Nhóm có một thành viên phụ trách ba vai theo README mục 3: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý.

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Hữu Phúc | 2A202603572 | Kỹ sư cổng; Sản phẩm và kinh doanh; Vận hành và pháp lý | Có |

Trường `members` trong [submission/submission.json](submission/submission.json) là `["BuiHuuPhuc-2A202603572"]`, khớp bảng trên; thẻ S7, v1 Tiếp tục, v2 Cải tiến thêm, ba dòng bắt buộc khớp [Phiếu C mục C12](templates/form-c-incident.md#c12). V2 hoãn pilot thật, không phải mở triển khai.

## Cá nhân

Mục cá nhân duy nhất của người thực hiện bài:

## BuiHuuPhuc-2A202603572

### Phần việc phụ trách

Phụ trách câu 1.1–1.6, 2.1–2.10 và 3.0–3.7; [Phiếu A](templates/form-a-criteria.md), [Phiếu B](templates/form-b-evaluation-gates.md), [Phiếu C](templates/form-c-incident.md), [cổng](lab10/guards.py), [monitor](lab10/monitors.py), [config vận hành](config/operating_gates.json), kiểm chứng và hồ sơ nộp. Ba vai được thực hiện lần lượt bởi một học viên.

### Đóng góp cụ thể

Phụ trách hồ sơ vòng 1 của nhóm: mục tiêu và tiêu chí chấp nhận; metric offline và telemetry; phân tích lỗi `T-002@55`, bản đồ dữ liệu, HAZOP và pre-mortem; ba cổng phòng ngừa; cấu hình kinh doanh/vận hành/pháp lý; runbook phần 1–3, phương án giờ cao điểm và quyết định v1. Dùng Codex hỗ trợ soạn nội dung, viết code và thực thi kiểm tra; các mã lần chạy và commit dưới đây là bằng chứng cho phần đã làm.

Vòng 2 chỉ S7: phân biệt copy customer_note với tự thêm recipient_contact từ DB, hiệu chỉnh lòng tin người đặt/người nhận, viết HAZOP và fault tree trước/sau, thêm audit cùng hai monitor, cập nhật checklist/runbook 4–5 và risk register. G3 vòng 1 đã ngăn hai đường lộ trên bộ visible; không ghi công vòng 2 làm giảm PII khi prepared vốn đã bằng 0. Chưa demo hoặc nhận phản biện từ bàn khác, chưa triển khai và chưa nộp LMS bằng tài khoản cá nhân.

### Bằng chứng

Commit tiêu chí: `791cf48`. Commit chốt vòng 1: `7d35cd9`. Baseline: `R-base-before-20261118-233821-bde05c`; prepared: `R-base-prepared-20261118-234324-d5398b`. Các lần thử cổng được ghi đầy đủ ở Phiếu B mục B0. Nguồn Lab 9 ở revision `70e5dd63c4fedfb861b3621f592eb415352298ca`; đối chiếu bổ sung ở cuối Phiếu A/B.

Nhận S7 tại commit `cd2ef92`. Grade trước sửa vòng 2: `R-S7-grade-20261119-011757-d5398b`; grade cuối: `R-S7-grade-20261119-012324-80b743`. S7 after 30/30 trong phạm vi, base after 65/65, không tác hại hoặc regression; 13 kiểm tra công khai và 6 kiểm tra runtime bổ sung đạt. Visible, criteria, regression, monitor đều đạt; **grade tổng FAIL ở integrity** vì manifest chung yêu cầu 28 file thẻ khác không có, trong khi cả 23 file khóa đang có đều đúng hash. Giữ riêng S7 đúng hướng dẫn học viên cung cấp; cần Coach xác nhận bộ kiểm phù hợp, không sửa grader/manifest. Hồ sơ ghi trung thực giới hạn này và v2 hoãn pilot, hạn quyết lại 20/11/2026 17:00 GMT+7.

Commit ký tiêu chí được tạo trước khi nhận MSSV nên mang tên Git cũ `phucbui66`; các commit đã có và thời điểm ký/đo được giữ nguyên để đối chiếu lịch sử.

### Exit ticket

- Một điều học được từ bài làm: pass_rate cao không thay thế kiểm tra an toàn trước lệnh ghi. Baseline Day 10 đạt 0,9909 nhưng vẫn hoàn sai 20.000đ và ghi oan 1 lỗi hãng; cần kiểm DB, quyền duyệt và sổ cái độc lập với lời khai/model.
- Một điều còn chưa chắc: bộ nền và MockLLM chưa chứng minh được cổng vẫn an toàn khi tải dồn, ghi đồng thời, drift chính sách hoặc dùng model thật. Cần kiểm chứng các tình huống này trước pilot người dùng thật.
- Bài học sau S7: ticket không chứa PII vẫn có thể lộ qua dữ liệu DB tự bổ sung; dựng lại payload từ trường được phép bảo vệ được cả hai đường, còn near-miss phải được phân biệt với dữ liệu đã thực sự gửi. Lỗi integrity do bộ phát/gói thẻ cần được xác nhận minh bạch, không tự lấy thẻ khác hoặc sửa bộ kiểm để tạo PASS.

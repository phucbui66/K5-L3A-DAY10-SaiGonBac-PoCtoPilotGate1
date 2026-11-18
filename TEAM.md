# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): SaiGonBac
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SaiGonBac-PoCtoPilotGate1`
- Hình thức thực hiện: **bài nhóm — nhóm có 1 thành viên**.
- Danh tính Git cho repo: `2A202603572` / `2A202603572@example.com`, theo hướng dẫn dùng MSSV và email giả.
- Thẻ sự cố đã bốc (S1–S8): **Chưa bốc; bổ sung khi bắt đầu vòng 2.**

## Thành viên

**Thành viên duy nhất và trưởng nhóm:** Bùi Hữu Phúc — MSSV `2A202603572`, đảm nhiệm cả ba vai của bài. Tên nhóm `SaiGonBac` khớp repo và tiêu chí đã ký. Hạnh, Tùng và Oanh là nhân vật vận hành giả trong tình huống LogiX-VN.

**Phạm vi lần làm này:** chỉ vòng 1, Phiếu A và Phiếu B đến quyết định v1; chưa nhận thẻ sự cố. Sau khi chốt v1, Phúc cung cấp repo Lab 9 và đã đối chiếu [PRD v1.1](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/PRD_v1.1.md), [eval card](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/eval_card.md) và [trace case](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/trace_case.md) tại revision `70e5dd63c4fedfb861b3621f592eb415352298ca`. Việc bổ sung nguồn không thay đổi tiêu chí, snapshot hay quyết định v1.

**Ghi nhận hỗ trợ AI:** bài nhóm do một thành viên thực hiện với Codex hỗ trợ đọc đề và code, soạn Phiếu A/B, đề xuất ngưỡng có lý do, viết và kiểm tra cổng vòng 1, đối chiếu nguồn Lab 9. Phúc chịu trách nhiệm về nội dung bài và việc giải thích các ngưỡng, cổng, quyết định khi trình bày.

Nhóm có một thành viên phụ trách ba vai theo README mục 3: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý.

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Hữu Phúc | 2A202603572 | Kỹ sư cổng; Sản phẩm và kinh doanh; Vận hành và pháp lý | Có |

Trường `members` trong [submission/submission.json](submission/submission.json) là `["BuiHuuPhuc-2A202603572"]`, khớp bảng trên. Tên repo, thành viên và quyết định v1 được điền trước; số thẻ, quyết định v2, ba dòng bắt buộc và bước gom bài thuộc phần sau sự cố.

## Cá nhân

Mục cá nhân duy nhất của người thực hiện bài:

## BuiHuuPhuc-2A202603572

### Phần việc phụ trách

Phụ trách toàn bộ vòng 1: câu 1.1–1.6 và 2.1–2.10; Phiếu A/B, `lab10/guards.py`, `config/operating_gates.json`, kiểm chứng và quyết định v1. Ba vai được thực hiện lần lượt bởi một học viên. Phiếu C và phần sự cố để làm sau.

### Đóng góp cụ thể

Phụ trách hồ sơ vòng 1 của nhóm: mục tiêu và tiêu chí chấp nhận; metric offline và telemetry; phân tích lỗi `T-002@55`, bản đồ dữ liệu, HAZOP và pre-mortem; ba cổng phòng ngừa; cấu hình kinh doanh/vận hành/pháp lý; runbook phần 1–3, phương án giờ cao điểm và quyết định v1. Dùng Codex hỗ trợ soạn nội dung, viết code và thực thi kiểm tra; các mã lần chạy và commit dưới đây là bằng chứng cho phần đã làm.

### Bằng chứng

Commit tiêu chí: `791cf48`. Commit chốt vòng 1: `7d35cd9`. Baseline: `R-base-before-20261118-233821-bde05c`; prepared: `R-base-prepared-20261118-234324-d5398b`. Các lần thử cổng được ghi đầy đủ ở Phiếu B mục B0. Nguồn Lab 9 ở revision `70e5dd63c4fedfb861b3621f592eb415352298ca`; đối chiếu bổ sung ở cuối Phiếu A/B.

Commit ký tiêu chí được tạo trước khi nhận MSSV nên mang tên Git cũ `phucbui66`; các commit đã có và thời điểm ký/đo được giữ nguyên để đối chiếu lịch sử.

### Exit ticket

- Một điều học được từ bài làm: pass_rate cao không thay thế kiểm tra an toàn trước lệnh ghi. Baseline Day 10 đạt 0,9909 nhưng vẫn hoàn sai 20.000đ và ghi oan 1 lỗi hãng; cần kiểm DB, quyền duyệt và sổ cái độc lập với lời khai/model.
- Một điều còn chưa chắc: bộ nền và MockLLM chưa chứng minh được cổng vẫn an toàn khi tải dồn, ghi đồng thời, drift chính sách hoặc dùng model thật. Cần kiểm chứng các tình huống này trước pilot người dùng thật.

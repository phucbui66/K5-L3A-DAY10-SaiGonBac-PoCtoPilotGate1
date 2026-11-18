# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): SaiGonBac
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-SaiGonBac-PoCtoPilotGate1`
- Hình thức thực hiện: **bài nhóm — nhóm có 1 thành viên**.
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

**Thành viên duy nhất và trưởng nhóm:** Bùi Hữu Phúc — MSSV `2A202603572`, đảm nhiệm cả ba vai của bài. Tên nhóm `SaiGonBac` khớp repo và tiêu chí đã ký. Hạnh, Tùng và Oanh là nhân vật vận hành giả trong tình huống LogiX-VN. Danh tính Git dùng MSSV và email do Phúc trực tiếp yêu cầu; đây là lựa chọn khác khuyến nghị email giả trong đề. Commit ký tiêu chí đã được đẩy trước khi nhận MSSV nên mang tên Git cũ `phucbui66` và email giả, giữ nguyên lịch sử này.

**Phạm vi lần làm này:** chỉ vòng 1, Phiếu A và Phiếu B đến quyết định v1; chưa nhận thẻ sự cố. Sau khi chốt v1, Phúc cung cấp repo Lab 9 và đã đối chiếu [PRD v1.1](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/PRD_v1.1.md), [eval card](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/eval_card.md) và [trace case](https://github.com/phucbui66/K5-L3A-Day9-BuiHuuPhuc-2A202603572-Evaluation-and-Failure-Analysis/blob/70e5dd63c4fedfb861b3621f592eb415352298ca/docs/trace_case.md) tại revision `70e5dd63c4fedfb861b3621f592eb415352298ca`. Việc bổ sung nguồn không thay đổi tiêu chí, snapshot hay quyết định v1.

**Ghi nhận hỗ trợ AI:** bài nhóm do một thành viên thực hiện với Codex hỗ trợ đọc đề và code, soạn Phiếu A/B, đề xuất ngưỡng có lý do, viết và kiểm tra cổng vòng 1, đối chiếu nguồn Lab 9. Phúc chịu trách nhiệm rà soát nội dung, giải thích từng ngưỡng và xác nhận phần tự đánh giá của mình trước khi nộp.

Nhóm có một thành viên phụ trách ba vai theo README mục 3: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý.

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Bùi Hữu Phúc | 2A202603572 | Kỹ sư cổng; Sản phẩm và kinh doanh; Vận hành và pháp lý | Có |

Khi làm bước gom bài cuối buổi, `members` trong `submission/submission.json` sẽ là `["BuiHuuPhuc-2A202603572"]`, khớp bảng trên. Bước gom bài được để sau phần sự cố theo phạm vi hiện tại.

## Cá nhân

Mục cá nhân duy nhất của người thực hiện bài:

## BuiHuuPhuc-2A202603572

### Phần việc phụ trách

Phụ trách toàn bộ vòng 1: câu 1.1–1.6 và 2.1–2.10; Phiếu A/B, `lab10/guards.py`, `config/operating_gates.json`, kiểm chứng và quyết định v1. Ba vai được thực hiện lần lượt bởi một học viên. Phiếu C và phần sự cố để làm sau.

### Đóng góp cụ thể

Thực hiện bài nhóm với hỗ trợ AI: Phúc cung cấp yêu cầu, danh tính học viên, xác nhận nhóm chỉ có một thành viên và nguồn Lab 9; Codex hỗ trợ soạn tiêu chí, phân tích trace/HAZOP, triển khai ba cổng, chạy kiểm tra, tổng hợp runbook và lưu bằng chứng. Phúc là người chịu trách nhiệm học thuật cho toàn bộ bài; mô tả này không khẳng định các bước do công cụ thực thi đều được gõ tay bởi học viên.

### Bằng chứng

Commit tiêu chí: `791cf48`. Commit chốt vòng 1: `7d35cd9`. Baseline: `R-base-before-20261118-233821-bde05c`; prepared: `R-base-prepared-20261118-234324-d5398b`. Các lần thử cổng được ghi đầy đủ ở Phiếu B mục B0. Nguồn Lab 9 ở revision `70e5dd63c4fedfb861b3621f592eb415352298ca`; đối chiếu bổ sung ở cuối Phiếu A/B.

### Exit ticket

**Bản nháp để Phúc tự rà soát và xác nhận:**

- Điều rút ra từ bằng chứng: pass_rate cao không thay thế kiểm tra an toàn trước lệnh ghi. Baseline Day 10 đạt 0,9909 nhưng vẫn hoàn sai 20.000đ và ghi oan 1 lỗi hãng; cần kiểm DB, quyền duyệt và sổ cái độc lập với lời khai/model.
- Điều còn cần kiểm chứng: bộ nền và MockLLM chưa chứng minh được hành vi khi tải dồn, ghi đồng thời, drift chính sách hoặc dùng model thật; cần dữ liệu và phép thử bổ sung trước pilot người dùng thật.

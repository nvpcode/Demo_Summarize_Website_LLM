# 📝 Website Summarizer

Dự án này cho phép bạn **tóm tắt nội dung của bất kỳ trang web nào** bằng cách:
- Trích xuất nội dung chính từ website (loại bỏ script, style, nav, footer,...).
- Gửi nội dung tới mô hình ngôn ngữ lớn (LLM) chạy qua Ollama.
- Trả về bản tóm tắt ngắn gọn, dễ hiểu, giữ nguyên ngôn ngữ gốc của website.

---

## 📂 Cấu trúc dự án
```
├── summarizer.py # Logic chính: lấy dữ liệu web + gọi LLM để tóm tắt
├── app.py # Giao diện web (Streamlit) để nhập URL và xem kết quả
```

---

## 🚀 Cách cài đặt và chạy

### 1. Cài đặt môi trường
Yêu cầu:
- Python >= 3.9
- [Ollama](https://ollama.ai/) (cài và khởi động server cục bộ)

Cài các thư viện cần thiết:
```
pip install streamlit requests beautifulsoup4 ollama
```

### 2. Chạy chương trình
Khởi chạy:
```
streamlit run app.py
```
Giao diện sẽ hiển thị tại địa chỉ:
👉 http://localhost:8501

Tại đây bạn có thể nhập URL website và nhận bản tóm tắt ngay trên trình duyệt.

## ⚙️ Cấu hình
Mô hình (MODEL): được định nghĩa trong summarizer.py, mặc định:
```
MODEL = "incept5/llama3.1-claude:latest"
```
Bạn có thể đổi sang model khác đã cài với Ollama.

Prompt hệ thống (SYSTEM_PROMPT):
```
SYSTEM_PROMPT = (
    "Bạn là trợ lý phân tích nội dung của một trang web. "
    "Và cung cấp một bản tóm tắt ngắn gọn, dễ hiểu. "
    "Nếu nội dung viết bằng ngôn ngữ nào thì hãy trả lời bằng ngôn ngữ đó. "
    "Trả lời dưới dạng markdown."
)
```
Có thể tùy chỉnh cho phù hợp nhu cầu.

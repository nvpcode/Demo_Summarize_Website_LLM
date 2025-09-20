import requests
from bs4 import BeautifulSoup
import ollama

# ==============================
# CẤU HÌNH
# ==============================
MODEL = "incept5/llama3.1-claude:latest"

SYSTEM_PROMPT = (
    """Bạn là trợ lý phân tích nội dung của một trang web.
    Và cung cấp một bản tóm tắt ngắn gọn, dễ hiểu.
    Nếu nội dung viết bằng ngôn ngữ nào thì hãy trả lời bằng ngôn ngữ đó.
    Trả lời dưới dạng markdown."""
)

# ==============================
# LỚP XỬ LÝ WEBSITE
# ==============================
class Website:
    def __init__(self, url: str):
        self.url = url
        self.title, self.text = self._scrape()

    def _scrape(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/120.0 Safari/537.36"
        }
        response = requests.get(self.url, headers=headers, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")

        # Lấy tiêu đề
        title = soup.title.string.strip() if soup.title and soup.title.string else "No title found"

        # Nếu không có body thì fallback toàn bộ text
        body = soup.body if soup.body else soup

        # Xóa các phần không cần thiết
        for irrelevant in body(["script", "style", "img", "input", "nav", "footer", "aside", "form", "noscript", "iframe"]):
            irrelevant.decompose()

        # Lấy nội dung text chính
        text = body.get_text(separator="\n", strip=True)
        return title, text


# ==============================
# PROMPT XÂY DỰNG
# ==============================
def user_prompt_for(website: Website) -> str:
    """
    Build the user prompt from a Website object
    """
    return (
        f"Bạn đang xem trang web có tiêu đề là {website.title}.\n\n"
        "Nội dung của trang web này như sau: "
        "Vui lòng cung cấp tóm tắt ngắn gọn về trang web này dưới dạng markdown."
        "Nếu trang web có tin tức hoặc thông báo, hãy tóm tắt cả những thông tin này nữa.\n\n"
        f"{website.text}"
    )


def messages_for(website: Website) -> list:
    """
    Build the conversation messages for the LLM
    """
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt_for(website)},
    ]


# ==============================
# TÓM TẮT
# ==============================
def summarize(url: str) -> str:
    """
    Summarize the website at the given URL
    """
    website = Website(url)
    messages = messages_for(website)
    response = ollama.chat(model=MODEL, messages=messages)
    return response["message"]["content"]

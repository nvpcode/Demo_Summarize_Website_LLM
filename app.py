import streamlit as st
from summarizer import summarize

st.set_page_config(page_title="Website Summarizer", layout="wide")
st.title("📝 Website Summarizer")

st.markdown(
    "Nhập một **URL** bất kỳ để hệ thống tự động lấy nội dung và tạo tóm tắt "
    "bằng mô hình LLM thông qua Ollama."
)

# Input URL
url = st.text_input("Nhập URL của website", value="https://github.com/nvpcode")
run_button = st.button("Tóm tắt")

if run_button and url:
    try:
        with st.spinner("⏳ Đang lấy nội dung và tóm tắt..."):
            summary = summarize(url)
        st.subheader("📌 Tóm tắt")
        st.markdown(summary)
    except Exception as e:
        st.error(f"⚠️ Lỗi: {e}")

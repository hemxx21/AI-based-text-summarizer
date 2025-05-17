# AI-based-text-summarizer
# 🧠 AI Text Summarizer

This is a simple yet effective command-line tool built in Python that summarizes content using the **Latent Semantic Analysis (LSA)** algorithm from the `sumy` library.

It allows users to extract and summarize text from:
- ✅ Custom text input
- ✅ Web article URLs
- ✅ Online research papers (PDF URLs)

Perfect for quick summarization tasks on lightweight systems like Raspberry Pi.

---

## ✨ Features

- 🔍 **Summarization using LSA**: Leverages `sumy`'s LSA summarizer to extract key points.
- 🌐 **Web scraping**: Extracts meaningful text from URLs (HTML pages).
- 📄 **PDF reader**: Downloads and parses online PDFs for summarization.
- 💻 **Runs on terminal**: No GUI needed. Works in SSH environments and low-resource devices.

---

## 🧩 Dependencies

Install all required Python packages with:

```bash
pip install -r requirements.txt

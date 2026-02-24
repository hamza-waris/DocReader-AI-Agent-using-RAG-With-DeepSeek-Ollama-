# 📘 DocReader AI Agent

An intelligent, local-first document assistant powered by **RAG (Retrieval-Augmented Generation)** using **DeepSeek LLM** via **Ollama** and **LangChain**. This app allows you to upload PDF documents and ask questions — getting concise, context-aware answers based on document content.

---

## 🚀 Features

- 📄 Upload and parse PDF documents
- ✂️ Smart text chunking using recursive splitting
- 🧠 Embedding + similarity search using InMemory Vector DB
- 💬 Chat-style interface powered by DeepSeek LLM (via Ollama)
- 🎨 Streamlit front-end with a dark, elegant custom theme

---

## 🧠 Tech Stack

| Component     | Tool/Library                |
|---------------|-----------------------------|
| Frontend      | Streamlit                   |
| LLM           | DeepSeek (via Ollama)       |
| RAG Pipeline  | LangChain                   |
| Embeddings    | `OllamaEmbeddings`          |
| Vector Store  | `InMemoryVectorStore`       |
| PDF Loader    | `PDFPlumberLoader`          |
| Styling       | Custom CSS (Streamlit)      |

---

## 📂 Folder Structure

DocReader-AI/
├── app.py # Main Streamlit app
├── document_store/
│ └── pdfs/ # Uploaded PDFs stored here
└── requirements.txt # Python dependencies


---

## ⚙️ How to Run Locally

> 🛑 Prerequisite: You must have [Ollama](https://ollama.com) and Python installed.

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate    # On Windows
# source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

Then open http://localhost:8501 in your browser.


🧠 Model Used
LLM: deepseek-r1:1.5b
Embedding Model: deepseek-r1:1.5b
All models are served locally via Ollama, enabling fast, secure, and offline-compatible document Q&A.

📌 Example Use Cases
Academic paper summarization

Legal/financial document QA

Internal documentation assistant

Research support tool

📃 License
MIT License. Use freely, modify locally.


🙋‍♂️ Author
Made with ❤️ by Awais Aslam


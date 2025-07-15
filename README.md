# 🧠 Research Paper Finder (RAG + Groq + Streamlit)

A lightweight, production-ready **Research Paper Finder** powered by:
- 🧠 **Retrieval-Augmented Generation (RAG)**
- 🚀 **Groq API with Llama 3.3 70B Versatile**
- 📚 **arXiv Integration**
- 💻 **FastAPI Backend**
- 🌐 **Streamlit Frontend UI**

> 🔗 **Live Demo**: [Explore the Research Paper Finder](https://khanfawaz-research-paper-finder.streamlit.app/)

---

## 📌 Features

✅ Natural language search over arXiv  
✅ Top 5 relevant research papers with author & source links  
✅ Child-level summaries generated using Groq LLM  
✅ RAG architecture (retrieval + generation)  
✅ FastAPI for optional API endpoints  
✅ Streamlit UI for live public demo  
✅ Docker-ready for deployment

---

## 🛠️ Tech Stack

| Layer       | Tools/Tech                              |
|-------------|------------------------------------------|
| 🧠 LLM       | [Groq API](https://groq.com/) with LLaMA 3.3 70B |
| 📚 Retrieval | [arXiv API](https://arxiv.org/help/api/) |
| 🧪 Backend   | [FastAPI](https://fastapi.tiangolo.com/) |
| 🎛️ Frontend | [Streamlit](https://streamlit.io/)        |
| 📦 Deploy    | Docker + GitHub + Streamlit Cloud        |

---

## 📂 Folder Structure

Research_Paper_Finder/
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── arxiv_utils.py
├── llm_utils.py
├── main.py # FastAPI backend (optional)
├── query_pipeline.py
├── requirements.txt
├── search_utils.py
└── streamlit_app.py # Main Streamlit entrypoint
from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict

from llm_utils import summarize_text
from search_utils import search_arxiv

app = FastAPI(
    title="Research Paper Finder",
    version="1.0.0",
    description="Finds and summarizes top 5 research papers using arXiv + Groq LLaMA 3.3"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Lock this down in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is healthy"}


@app.get("/query")
def query_papers(keyword: str = Query(..., description="Search keyword for academic papers")):
    try:
        papers = search_arxiv(keyword)
        summarized_results = []

        for paper in papers:
            summary = summarize_text(paper["abstract"])
            summarized_results.append({
                "title": paper["title"],
                "summary": summary,
                "source": paper["source"],
                "authors": paper["authors"],
                "published": paper["published"]
            })

        return {
            "query": keyword,
            "results": summarized_results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

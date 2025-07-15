from arxiv_utils import search_arxiv
from llm_utils import summarize_text

def run_full_query_pipeline(keyword: str) -> dict:
    papers = search_arxiv(keyword)
    summarized_results = []

    for paper in papers:
        summary = summarize_text(paper["abstract"])
        summarized_results.append({
            "title": paper["title"],
            "summary": summary,
            "source": paper["source"],
            "authors": paper["authors"],
            "published": paper["published"],
        })

    return {
        "query": keyword,
        "results": summarized_results
    }

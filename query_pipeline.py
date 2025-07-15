from typing import Optional, List
from arxiv_utils import search_arxiv
from llm_utils import summarize_text

def run_full_query_pipeline(
    keyword: str,
    input_type: str = "topic",
    source: str = "arxiv",
    year_filter: Optional[int] = None
) -> List[dict]:
    if source == "arxiv":
        papers = search_arxiv(keyword, input_type=input_type, year_filter=year_filter)
    else:
        raise ValueError(f"Unsupported source: {source}")

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

    return summarized_results

from typing import Optional, List
from arxiv_utils import search_arxiv
from llm_utils import summarize_text

def run_full_query_pipeline(
    keyword: str,
    input_type: str = "topic",
    source: str = "arxiv",
    year_filter: Optional[int] = None
) -> List[dict]:
    all_results = []

    if source.lower() in ["arxiv", "all"]:
        papers = search_arxiv(keyword, input_type=input_type, year_filter=year_filter)
        for paper in papers:
            summary = summarize_text(paper["abstract"])
            all_results.append({
                "title": paper["title"],
                "summary": summary,
                "source": paper["source"],
                "authors": paper["authors"],
                "published": paper["published"],
            })

    # Placeholder for future sources (e.g., IEEE, PubMed)
    # elif source.lower() == "pubmed":
    #     papers = search_pubmed(...)
    #     ...

    if not all_results:
        raise ValueError(f"Unsupported source: {source}")

    return all_results

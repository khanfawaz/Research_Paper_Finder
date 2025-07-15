from typing import List, Optional
import arxiv
import datetime

def search_arxiv(keyword: str, input_type: str = "topic", year_filter: Optional[int] = None) -> List[dict]:
    search_query = keyword.strip()
    
    # Extendable logic for other input types
    if input_type.lower() == "question":
        search_query = keyword.replace("?", "")
    elif input_type.lower() == "keyword":
        search_query = keyword.strip()

    search = arxiv.Search(
        query=search_query,
        max_results=10,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    results = []
    for result in search.results():
        if year_filter:
            published_year = result.published.year
            if published_year < year_filter:
                continue

        results.append({
            "title": result.title,
            "abstract": result.summary,
            "authors": [author.name for author in result.authors],
            "published": result.published.isoformat(),
            "source": result.entry_id
        })

    return results
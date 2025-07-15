# search_utils.py

import httpx
from typing import List, Dict
from xml.etree import ElementTree as ET


def search_arxiv(query: str, max_results: int = 5) -> List[Dict]:
    """
    Search arXiv for papers matching the query and return top N results.
    """
    url = f"https://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results={max_results}"

    response = httpx.get(url, timeout=10)
    if response.status_code != 200:
        raise Exception(f"arXiv API error: {response.status_code}")

    root = ET.fromstring(response.content)

    ns = {'arxiv': 'http://www.w3.org/2005/Atom'}
    results = []

    for entry in root.findall('arxiv:entry', ns):
        title = entry.find('arxiv:title', ns).text.strip().replace('\n', ' ')
        summary = entry.find('arxiv:summary', ns).text.strip().replace('\n', ' ')
        published = entry.find('arxiv:published', ns).text.strip()
        link = entry.find('arxiv:id', ns).text.strip()

        authors = []
        for author in entry.findall('arxiv:author', ns):
            name = author.find('arxiv:name', ns).text.strip()
            authors.append(name)

        results.append({
            "title": title,
            "abstract": summary,
            "published": published,
            "source": link,
            "authors": authors
        })

    return results

import requests
import xml.etree.ElementTree as ET

def search_arxiv(query: str, max_results: int = 5):
    base_url = "http://export.arxiv.org/api/query"
    params = {
        "search_query": query,
        "start": 0,
        "max_results": max_results
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}

    papers = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        abstract = entry.find('atom:summary', ns).text.strip()
        published = entry.find('atom:published', ns).text.strip()
        link = entry.find('atom:id', ns).text.strip()
        authors = [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]

        papers.append({
            "title": title,
            "abstract": abstract,
            "published": published,
            "source": link,
            "authors": authors,
        })

    return papers

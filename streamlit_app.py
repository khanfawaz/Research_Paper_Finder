import streamlit as st
from query_pipeline import run_full_query_pipeline  # You already have this in FastAPI

st.set_page_config(page_title="Research Paper Finder", layout="wide")

st.title("🔍 Research Paper Finder")
st.write("Enter a research topic to discover the top 5 most relevant academic papers.")

query = st.text_input("Enter keyword (e.g., quantum cryptography):", "")

if st.button("Search") and query:
    with st.spinner("Searching and summarizing..."):
        result = run_full_query_pipeline(query)
        for idx, paper in enumerate(result['results'], start=1):
            st.markdown(f"### {idx}. {paper['title']}")
            st.markdown(f"**Authors**: {', '.join(paper['authors'])}")
            st.markdown(f"**Published**: {paper['published']}")
            st.markdown(f"**Source**: [Link]({paper['source']})")
            st.markdown(f"**Summary**: {paper['summary']}")
            st.markdown("---")

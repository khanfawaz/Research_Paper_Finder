import streamlit as st
from query_pipeline import run_full_query_pipeline
import datetime

st.set_page_config(page_title="Research Paper Finder", layout="wide")
st.title("📄 Research Paper Finder (AI + RAG Powered)")

# Sidebar filters
st.sidebar.header("🔍 Search Filters")

# Search input
search_input = st.sidebar.text_input("Enter Keyword / Topic / Question", value="quantum cryptography")

# Input type selection (currently not functional, placeholder for future)
input_type = st.sidebar.selectbox("Input Type", ["Keyword", "Topic", "Question"])

# Publication Source selection
source = st.sidebar.selectbox("Preferred Publication Source", ["arXiv", "PubMed", "IEEE", "Springer", "All"])

# Year filter selection
year_filter = st.sidebar.selectbox("Filter by Year", ["All", "Last 1 Year", "Last 3 Years", "Last 5 Years"])

# Convert year selection to year value
current_year = datetime.datetime.now().year
year_cutoff_map = {
    "All": None,
    "Last 1 Year": current_year - 1,
    "Last 3 Years": current_year - 3,
    "Last 5 Years": current_year - 5
}
year_cutoff = year_cutoff_map[year_filter]

# Trigger search
if st.sidebar.button("🔎 Search Research Papers"):
    if not search_input:
        st.warning("Please enter a keyword or topic.")
    else:
        with st.spinner("Searching and summarizing papers..."):
            try:
                results = run_full_query_pipeline(
                    keyword=search_input,
                    source=source,
                    year_filter=year_cutoff
                )

                if results:
                    st.success(f"Found {len(results)} results for: '{search_input}'")
                    for paper in results:
                        st.markdown(f"### {paper['title']}")
                        st.markdown(f"**Authors:** {', '.join(paper['authors'])}")
                        st.markdown(f"**Published:** {paper['published'][:10]}")
                        st.markdown(f"**Summary:** {paper['summary']}")
                        st.markdown(f"[{paper['source']}]({paper['source']})", unsafe_allow_html=True)
                        st.markdown("---")
                else:
                    st.warning("No results found. Try different keywords or filters.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
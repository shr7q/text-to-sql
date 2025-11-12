# Build streamlit frontend
import streamlit as st
from app import get_data_from_database

# Configure the Streamlit app page settings
st.set_page_config(
    page_title="Text to SQL with Deepseek and Ollama", # App title
    page_icon="🎯",                                   # App icon
    layout="centered"                                 # Layout
)

#  Display main title header
st.title("Text to SQL with Deepseek and Ollama")

# Display app description
st.markdown("Ask questions about your data in natural language.")

# Text area for user query input
user_query = st.text_area("Enter your query:", placeholder="e.g., Total products sold in 2025")

if st.button("Enter"):
    if user_query.strip() == "":
        st.warning("Please enter a question to analyze.")
    else:
        with st.spinner("Analyzing your query..."):
            database_response = get_data_from_database(user_query)
            fixed_answer = f"Results to your query:\n\n**{database_response}**"

        st.success("Analysis complete!")
        st.markdown(fixed_answer)

# Custom CSS styling to increase textarea font size for better usability
st.markdown("""
    <style>
    textarea {
        font-size: 16px !important;
    }
    </style>
""", unsafe_allow_html=True)
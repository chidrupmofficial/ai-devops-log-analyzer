import streamlit as st

st.title("AI DevOps Log Analyzer")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("Log Content")
    st.text(content)
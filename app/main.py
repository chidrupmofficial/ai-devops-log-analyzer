import streamlit as st

st.title("AI DevOps Log Analyzer")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:
    content = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("Log Content")
    st.text(content)

    st.subheader("Detected Issues")

    lines = content.splitlines()

    for line in lines:
        if "ERROR" in line:
            st.error(line)

        elif "WARN" in line:
            st.warning(line)

        elif "FAILED" in line:
            st.error(line)

        elif "Exception" in line:
            st.exception(line)
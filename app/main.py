import streamlit as st
import pandas as pd

st.title("AI DevOps Log Analyzer")

uploaded_file = st.file_uploader("Upload a log file")

if uploaded_file:

    content = uploaded_file.read().decode("utf-8", errors="ignore")

    st.subheader("Log Content")
    st.text(content)

    lines = content.splitlines()

    error_count = 0
    warn_count = 0
    failed_count = 0
    exception_count = 0

    st.subheader("Detected Issues")

    for line in lines:

        if "ERROR" in line:
            error_count += 1
            st.error(line)

        elif "WARN" in line:
            warn_count += 1
            st.warning(line)

        elif "FAILED" in line:
            failed_count += 1
            st.error(line)

        elif "Exception" in line:
            exception_count += 1
            st.exception(line)

    st.subheader("Issue Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Errors", error_count)
    col2.metric("Warnings", warn_count)
    col3.metric("Failures", failed_count)
    col4.metric("Exceptions", exception_count)

    st.subheader("AI Root Cause Analysis")

    if error_count > 0:

        if "Kubernetes" in content:
            st.info("Possible Cause: Kubernetes pod crash detected.")

        if "Docker" in content:
            st.info("Possible Cause: Docker container failure detected.")

        if "memory" in content.lower():
            st.info("Possible Cause: High memory usage may have caused failure.")

        if "disk" in content.lower():
            st.info("Possible Cause: Disk space issue detected.")

        if "Jenkins" in content:
            st.info("Possible Cause: CI/CD pipeline execution failed.")
            
    st.subheader("Issue Severity Dashboard")

    chart_data = pd.DataFrame(
        {
            "Issue Type": ["Errors", "Warnings", "Failures", "Exceptions"],
            "Count": [error_count, warn_count, failed_count, exception_count],
        }
    )

    st.bar_chart(chart_data.set_index("Issue Type"))        
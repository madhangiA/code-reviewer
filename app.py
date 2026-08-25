import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

from services.code_reviewer import review_code

from utils.formatter import (
    generate_pdf,
    extract_score,
    extract_fixed_code,
    extract_severity,
    format_for_pdf
)

load_dotenv()
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Code Reviewer")

st.write(
    "Paste your code below and receive bug reports, quality scores, suggestions, and fixed code."
)

# Language Selection

language = st.selectbox(
    "Select Programming Language",
    [
        "Python",
        "Java",
        "JavaScript",
        "C++",
        "SQL"
    ]
)

# Code Input

user_code = st.text_area(
    "Enter Code",
    height=300
)

# Review Button

if st.button("Review Code"):

    if not user_code.strip():
        st.warning("Please enter code.")
    else:

        with st.spinner("Reviewing code..."):
            try:
                result = review_code(
                    user_code,
                    language
                )
            except RuntimeError as exc:
                st.error(str(exc))
                st.stop()

        st.success("Review Complete")

        # Display Quality Score

        score = extract_score(result)

        if score is not None:
            st.metric(
                "Code Quality Score",
                f"{score}/10"
            )

        # Display Severity Levels

        severity = extract_severity(result)

        if severity:
            st.warning(
                f"Severity Levels Found: {', '.join(severity)}"
            )

        # Full Review

        st.subheader("Review Report")

        st.markdown(result)

        # Fixed Code

        fixed_code = extract_fixed_code(result)

        if fixed_code:

            st.subheader("Fixed Code")

            st.code(
                fixed_code,
                language=language.lower()
            )

        # Generate PDF Content

        pdf_content = format_for_pdf(
            user_code,
            language,
            result
        )

        pdf_file = generate_pdf(
            pdf_content
        )

        # Download Button

        with open(pdf_file, "rb") as file:

            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="code_review_report.pdf",
                mime="application/pdf"
            )
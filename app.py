import streamlit as st
from parser import extract_text_from_pdf, extract_text_from_docx
from ranker import rank_candidates
import pandas as pd

st.set_page_config(page_title="Intelligent Candidate Ranking", layout="wide")
st.title("🤖 Intelligent Candidate Ranking Engine")
st.write("**Track 1: Datathon Arena | INDIA.RUNS**")

jd_text = st.text_area("Paste Job Description Here", height=200)
uploaded_files = st.file_uploader("Upload Resumes (PDF/DOCX)", accept_multiple_files=True)

if st.button("Rank Candidates", type="primary"):
    if jd_text and uploaded_files:
        with st.spinner("Ranking in progress..."):
            resume_texts, names = [], []
            for file in uploaded_files:
                if file.name.endswith('.pdf'):
                    text = extract_text_from_pdf(file)
                else:
                    text = extract_text_from_docx(file)
                resume_texts.append(text)
                names.append(file.name.replace('.pdf','').replace('.docx',''))
            
            results = rank_candidates(jd_text, resume_texts, names)
            st.success("Ranking Complete!")
            st.dataframe(pd.DataFrame(results), use_container_width=True)
    else:
        st.error("Please provide JD and upload resumes")
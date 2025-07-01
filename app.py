# app.py
import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

st.title("📝 Text Summarizer")
text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
            st.success("Summary:")
            st.write(summary[0]["summary_text"])

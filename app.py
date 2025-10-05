import streamlit as st
from main import fetch_article_text, summarize_text

# Streamlit UI
st.set_page_config(page_title="AI Article Summarizer", page_icon="📰", layout="centered")

st.title("📰 AI Article Summarizer")
st.write("Enter a blog/news URL and get a concise summary powered by **Groq Llama-3.3-70b** 🚀")

url = st.text_input("Enter Article URL:")

if st.button("Summarize"):
    if url.strip() == "":
        st.warning("⚠️ Please enter a valid URL.")
    else:
        with st.spinner("Fetching article..."):
            article_text = fetch_article_text(url)

        if "Error" in article_text or len(article_text) < 100:
            st.error("❌ Could not fetch enough article content. Please try another link.")
        else:
            with st.spinner("Summarizing with Groq..."):
                summary = summarize_text(article_text)

            st.subheader("🔎 Summary:")
            st.success(summary)

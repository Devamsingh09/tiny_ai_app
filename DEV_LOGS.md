
# Development Log — tiny_ai_app

This document records all steps, experiments, and learnings during the creation of **tiny_ai_app**, a small AI-powered summarization tool built as part of the *Tiny AI App Assignment*.

---

## Step 1 — Setup

- Installed **Python 3.11.7** and created a virtual environment:
  ```bash
  python -m venv venv
  venv\Scripts\activate  # for Windows
````

* Installed required dependencies:

  ```bash
  pip install requests beautifulsoup4 python-dotenv groq streamlit
  ```

* Created a GitHub repository:
  👉 [tiny_ai_app](https://github.com/Devamsingh09/tiny_ai_app)

* Initial project structure:

  ```
  tiny_ai_app/
  ├── main.py         # Core summarization logic
  ├── app.py          # Streamlit app for UI
  ├── .env
  ├── requirements.txt
  ├── README.md
  └── DEV_LOG.md
  ```

---

## Step 2 — API Exploration & Failures

Before selecting **Groq**, I experimented with multiple APIs and model providers to understand performance, latency, and ease of use.

### 🧠 Attempt 1 — Hugging Face Inference API

* Tried Hugging Face’s summarization models.
* Issue: **Very high inference time** (30–60 seconds per request).
* Required token authentication and had strict rate limits.
* Dropped due to performance and quota restrictions.

### 🤖 Attempt 2 — Anthropic (Claude)

* Attempted to use **Anthropic’s Claude 3 API**.
* Could not access due to **no free-tier availability** and **billing setup requirement**.
* Not suitable for this open project.

### 🧩 Attempt 3 — OpenRouter API

* Found **OpenRouter**, an aggregator of multiple open models.
* Looked flexible, but had **complex request headers** and **routing configuration**.
* Multiple requests failed due to misconfigured authorization tokens.
* Decided to move on due to complexity.

### 🔍 Decision — Try Groq API

* In previous projects, I had used **Gemini API**, so I wanted to try something new.
* Heard about **Groq API** for its **ultra-low latency** and **Llama 3 model support**.
* Signed up for a Groq account, generated an API key, and started testing.
* Worked flawlessly with simple integration and great speed.

---

## Step 3 — Groq API Setup

* Created `.env` file for secure API key storage:

  ```env
  GROQ_API_KEY=your_groq_api_key_here
  ```

* Loaded environment variables in Python:

  ```python
  from dotenv import load_dotenv
  import os
  load_dotenv()
  api_key = os.getenv("GROQ_API_KEY")
  ```

* Initialized Groq client using the key:

  ```python
  from groq import Groq
  client = Groq(api_key=api_key)
  ```

---

## Step 4 — Core Logic (`main.py`)

The `main.py` file handles:

* Fetching and cleaning text from any given URL.
* Sending the cleaned text to the **Groq Llama 3.3-70B model** for summarization.
* Returning a 3-sentence summary.

### Core Functions:

```python
def fetch_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    return " ".join([p.get_text() for p in paragraphs]).strip()

def summarize_text(text):
    prompt = f"Summarize in 3 sentences:\n\n{text}"
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )
    return chat_completion.choices[0].message.content
```

✅ Successfully generated summaries with excellent speed and coherence.

---

## Step 5 — Streamlit Interface (`app.py`)

Built a simple web interface using **Streamlit** so the app can be easily accessed and tested.

### Features:

* User inputs a blog/news URL.
* App fetches and summarizes the content using `main.py` functions.
* Displays the clean 3-sentence summary.

```python
import streamlit as st
from main import fetch_article_text, summarize_text

st.title("🧠 AI Article Summarizer")
url = st.text_input("Enter a news/blog URL:")

if st.button("Summarize"):
    with st.spinner("Fetching and summarizing..."):
        text = fetch_article_text(url)
        if "Error" in text:
            st.error(text)
        else:
            summary = summarize_text(text)
            st.subheader("📄 Summary")
            st.write(summary)
```

Run locally:

```bash
streamlit run app.py
```

---

## Step 6 — Error Handling & Refinements

Added safeguards for:

* Empty/invalid URLs
* Network errors
* API call exceptions

Improved user experience with formatted messages in Streamlit and console.

---

## Step 7 — Deployment

### GitHub:

Pushed all project files:

```bash
git init
git add .
git commit -m "Initial commit for tiny_ai_app"
git branch -M main
git remote add origin https://github.com/Devamsingh09/tiny_ai_app.git
git push -u origin main
```

### Streamlit Cloud:

* Connected GitHub repo directly.
* Added `GROQ_API_KEY` in **Streamlit Secrets** (Settings → Secrets).
* Deployed successfully — app builds automatically on every commit.

✅ App fully functional and public on Streamlit Cloud.

---

## Step 8 — Testing

Tested with various sources:

* TechCrunch articles
* Medium blogs
* NDTV and BBC news posts

Observations:

* Groq API delivered fast responses.
* Summaries remained concise and meaningful.
* No token limit issues on normal-length articles.

---

## Step 9 — Learnings

* Explored **different model APIs** (Hugging Face, Anthropic, OpenRouter, Groq).
* Learned **why response latency matters** in API selection.
* Understood **environment variable management** locally and on cloud.
* Gained experience with **Streamlit deployment workflow**.
* Reinforced debugging skills and error handling practices.

---

## Step 10 — Future Enhancements

* Add summarization modes: *Brief*, *Detailed*, *Bullet Points*.
* Display article metadata (title, author, date).
* Add file upload support for text or PDF summarization.
* Option to download summary as `.txt` or `.pdf`.

---

## 🧩 Workflow Diagram (Text-Based)

```
┌─────────────────────────────┐
│        User Inputs URL      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Fetch & Clean Text (main.py)│
│  → BeautifulSoup Scraper    │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Summarize via Groq API      │
│  → Llama 3.3-70B Model      │
└──────────────┬──────────────┘
               │
               ▼
┌─────────────────────────────┐
│ Display Summary (Streamlit) │
│  → app.py                   │
└─────────────────────────────┘
```

---

✅ **Final Project Link:**
[GitHub Repo — tiny_ai_app](https://github.com/Devamsingh09/tiny_ai_app)

✅ **Live Streamlit App:**
*[https://devamsingh.streamlit.app/](https://devamsingh.streamlit.app/)*

```
```

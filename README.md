

# 🧠 tiny_ai_app — AI-Powered Article Summarizer

An intelligent **AI summarization app** that fetches any article or blog post from the web and summarizes it into **3 concise sentences** using **Groq’s Llama 3.3-70B model**.

This project was built as part of the **Tiny AI App Assignment**, showcasing creativity, problem-solving, and exploration of multiple AI APIs.

---

## 🚀 Features

- 🌐 Fetches and cleans article text directly from a URL  
- 🤖 Summarizes using **Groq’s Llama 3.3-70B** (ultra-low latency)  
- 💬 3-sentence summaries that stay factual and concise  
- ⚙️ Built with **Python**, **BeautifulSoup**, and **Streamlit**  
- 🔐 Uses `.env` or Streamlit Secrets for secure API key management  

---

## 🧩 Workflow

<img width="300" height="300" alt="Gemini_Generated_Image_kz28rzkz28rzkz28" src="https://github.com/user-attachments/assets/34751666-2c0e-4271-82dc-ed8e0b486de8" />


## 🛠️ Tech Stack

- **Python 3.11**
- **Groq API** for summarization  
- **BeautifulSoup4** for web scraping  
- **Streamlit** for UI  
- **dotenv** for environment variable management  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Devamsingh09/tiny_ai_app.git
cd tiny_ai_app
````

### 2️⃣ Create & activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # for Windows
# or
source venv/bin/activate  # for macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set up your Groq API Key

#### Option A: Using `.env` file (local)

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

#### Option B: Using Streamlit Cloud

* Go to your Streamlit app dashboard
* Open **Settings → Secrets**
* Add:

  ```toml
  GROQ_API_KEY = "your_groq_api_key_here"
  ```

---

## ▶️ How to Use

### 💻 Run Locally (Command Line)

```bash
python main.py
```

Then enter a blog/news URL when prompted.

### 🌐 Run via Streamlit (Web App)

```bash
streamlit run app.py
```

Paste your article URL and click **Summarize** to see the AI-generated summary.

---

## 🧠 Example Output

**Input:**

> [https://techcrunch.com/2025/01/10/some-latest-ai-research-breakthrough/](https://techcrunch.com/2025/01/10/some-latest-ai-research-breakthrough/)

**Output Summary:**

> The article discusses recent advancements in AI research.
> It highlights new models with faster inference and improved accuracy.
> Experts predict wide-ranging applications across industries.

---

## 🧭 Development Journey (Documented Steps)

This project went through several iterations and experiments before reaching its final version.

### 🔍 API Trials & Learnings

| Attempt            | API / Model                                                 | Outcome |
| ------------------ | ----------------------------------------------------------- | ------- |
| Hugging Face       | Worked but **inference was too slow** (30–60 sec).          |         |
| Anthropic (Claude) | No **free-tier access**, required billing setup.            |         |
| OpenRouter         | **Complex API setup**, token auth issues.                   |         |
| Gemini             | Used before in other projects; wanted to try something new. |         |
| Groq               | ✅ **Fast**, reliable, and easy to integrate — final choice. |         |

---

## 🧱 Project Structure

```
tiny_ai_app/
├── app.py              # Streamlit interface
├── main.py             # Core logic (fetch + summarize)
├── requirements.txt    # Dependencies
├── .env                # API key (local)
├── DEV_LOG.md          # Full development documentation
└── README.md           # Project overview
```

---

## 🧪 Testing

* Tested with **TechCrunch**, **BBC**, **NDTV**, and **Medium** articles
* Observed **fast responses (<3s)** with Groq API
* Summaries remained **coherent and accurate**

---

## 🌍 Deployment

✅ **Deployed successfully on Streamlit Cloud**

* App auto-builds from GitHub repo
* API key managed via Streamlit Secrets
* Quick and stable performance

**Live App Link:**
👉 *(Add your Streamlit Cloud link here)*

---

## 🚧 Future Enhancements

* Add **multiple summary modes** (Brief / Detailed / Bullet points)
* Display **article metadata** (title, author, date)
* Add **file upload** for PDFs or text files
* Enable **summary downloads** as `.txt` or `.pdf`

---

## 💬 Author

👨‍💻 **Devam Singh**
📂 [GitHub — Devamsingh09](https://github.com/Devamsingh09)
📧 *Reach out for collaboration or suggestions!*

---

### ⭐ If you found this project helpful, please give it a star on GitHub!

```



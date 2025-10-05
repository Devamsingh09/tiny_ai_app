import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Choose the model (Llama 3.3B for summarization)
MODEL_NAME = "llama-3.3-70b-versatile"



def fetch_article_text(url):
    """Fetch and clean article text from URL"""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        article_text = " ".join([p.get_text() for p in paragraphs])
        return article_text.strip()
    except Exception as e:
        return f"Error fetching article: {e}"

def summarize_text(text):
    """Summarize the full article text using Groq API"""
    prompt = f"Summarize the following text into 3 sentences:\n\n{text}"
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME
        )
        summary = chat_completion.choices[0].message.content
        return summary
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = input("Enter a news/blog URL: ")
    article_text = fetch_article_text(url)

    if "Error" in article_text:
        print(article_text)
    else:
        print("\n--- Article Summary ---")
        summary = summarize_text(article_text)
        print(summary)

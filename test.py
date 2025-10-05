from dotenv import load_dotenv
load_dotenv(override=True)
import os
print("GROQ_API_KEY:", os.getenv("GROQ_API_KEY"))

# llm_utils.py

import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

def summarize_text(text: str) -> str:
    """
    Takes a long text (like a research abstract) and returns a summary using Groq LLaMA 3.3.
    """
    prompt = f"Summarize the following research abstract in simple terms:\n\n{text}"

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Updated model name
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=512,
        top_p=1,
        stream=False
    )

    return completion.choices[0].message.content.strip()

print("Loaded GROQ API Key:", GROQ_API_KEY)
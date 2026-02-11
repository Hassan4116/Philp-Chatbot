from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=OPENAI_API_KEY)

ROUTER_PROMPT = """
You are Philp Router.
Your ONLY job is to classify user intent.

Return ONLY one word from:
general
coder
teacher
summarizer

Rules:
- Coding questions → coder
- Asking to explain → teacher
- Asking to summarize → summarizer
- Everything else → general

User message:
"""

def detect_mode(message: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": ROUTER_PROMPT},
                      {"role": "user", "content": message}],
            temperature=0.0
        )
        mode = response.choices[0].message.content.strip().lower()
        if mode in ["general", "coder", "teacher", "summarizer"]:
            return mode
        return "general"
    except Exception as e:
        print(f"Router error: {str(e)}")
        return "general"
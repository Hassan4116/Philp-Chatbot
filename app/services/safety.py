from app.config import OPENAI_API_KEY
from openai import OpenAI

client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=OPENAI_API_KEY)

SAFETY_PROMPT = """
You are a safety filter for Philp.
You understand the user's language: {language}.
Return "safe" if the message is safe.
Return "unsafe" if it contains:
- Hate, harassment
- Violence or threats
- Adult content
- Illegal instructions
- Self-harm instructions

User Message:
"""

def is_safe(message: str, language: str) -> bool:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SAFETY_PROMPT.replace("{language}", language)},
            {"role": "user", "content": message}
        ],
        temperature=0
    )

    verdict = response.choices[0].message.content.strip().lower()
    return verdict == "safe"
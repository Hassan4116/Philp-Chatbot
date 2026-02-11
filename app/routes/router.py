from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=OPENAI_API_KEY)

ROUTER_PROMPT = """
You are Philp Router.
Classify the user's message and detect language.

Return a JSON ONLY with two keys:
{
  "mode": "general | coder | teacher | summarizer | tools | rag",
  "language": "<ISO 639-1 language code>"
}

Rules for mode:
- Coding question → coder
- Asking to explain → teacher
- Asking to summarize → summarizer
- Asking to use tools or APIs → tools
- Asking to answer from documents → rag
- Everything else → general

Rules for language:
- Detect the language of the message accurately.
- Return standard 2-letter ISO code (en, fr, es, etc.)

User message:
"""

def detect_mode_and_language(message: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": ROUTER_PROMPT},
                      {"role": "user", "content": message}],
            temperature=0.0
        )
        try:
            import json
            data = json.loads(response.choices[0].message.content.strip())
            mode = data.get("mode", "general")
            language = data.get("language", "en")
            allowed_modes = ["general", "coder", "teacher", "summarizer", "tools", "rag"]
            if mode not in allowed_modes:
                return "general"
            return {"mode": mode, "language": language}
        except Exception:
            return {"mode": "general", "language": "en"}
    except Exception as e:
        print(f"Router error: {str(e)}")
        return {"mode": "general", "language": "en"}
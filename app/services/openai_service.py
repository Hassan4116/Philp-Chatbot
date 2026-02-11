from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.services.memory import get_history, save_message


client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are Philp – a friendly AI assistant.

Personality:
- Friendly and natural
- Not too long answers
- If you don't know, say you don't know
- You remember conversation

Goal:
Help the user while being simple and clear.
"""

def get_philp_reply(message: str, session_id: str) -> str:
    try:
        save_message(session_id, "user", message)

        history = get_history(session_id)

        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages += history

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content.strip()

        save_message(session_id, "assistant", reply)

        return reply

    except Exception as e:
        return f"Philp error: {str(e)}"
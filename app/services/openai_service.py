from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.services.memory import get_history, save_message
from app.services.prompts import get_prompt


client = OpenAI(base_url="https://api.groq.com/openai/v1",api_key=OPENAI_API_KEY)


def get_philp_reply(message: str, session_id: str, mode: str) -> str:
    try:
        save_message(session_id, "user", message)

        history = get_history(session_id)

        system_prompt = get_prompt(mode)

        messages = [{"role": "system", "content": system_prompt}]
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
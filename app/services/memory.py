conversation = {}

def get_history(session_id: str):
    return conversation.get(session_id, [])

def save_message(session_id: str, role: str, content: str):
    if session_id not in conversation:
        conversation[session_id] = []

    conversation[session_id].append({
        "role": role,
        "content": content
    })
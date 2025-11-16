import requests

url = "https://ffb7b115d7a7.ngrok-free.app/generate"

history = []
system_prompt = """You are a smart, accurate, helpful assistant.
- Answer the user's questions directly and concisely.
- Do not invent extra messages or conversations."""
print("Chat with AI. Type an empty line to exit.")

while True:
    user_prompt = input("\nYou: ").strip()
    if not user_prompt:
        break

    full_prompt = system_prompt + "\n\nConversation history:\n"
    for msg in history:
        full_prompt += msg + "\n"
    full_prompt += f"User: {user_prompt}\nAI:"

    payload = {"prompt": full_prompt}
    resp = requests.post(url, json=payload)
    if resp.ok:
        try:
            result = resp.json()
            raw_response = result.get('text') or result.get('response') or str(result)
            ai_response = raw_response.rsplit('AI:', 1)[-1].strip()
        except Exception:
            ai_response = resp.text.strip()
    else:
        ai_response = f"Error {resp.status_code}: {resp.text[:200]}"

    print(f"AI: {ai_response}")
    history.append(f"User: {user_prompt}")
    history.append(f"AI: {ai_response}")
    if len(history) > 20:
        history = history[-20:]

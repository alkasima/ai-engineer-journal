import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Keep conversation history
conversation_history = []

def ask_ai(prompt):
    global conversation_history
    
    # Append user message to conversation history
    conversation_history.append({"role": "user", "content": prompt})

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": conversation_history
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise error for bad status codes
        result = response.json()

        if "choices" in result and len(result["choices"]) > 0:
            ai_message = result["choices"][0]["message"]["content"]
            # Append AI response to conversation history
            conversation_history.append({"role": "assistant", "content": ai_message})
            return ai_message
        else:
            return f"Error: Unexpected API response {result}"

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# --- CHAT SYSTEM ---
print("Welcome to your AI Chat! Type 'exit' to quit, '/reset' to clear history")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    elif user_input.lower() == "/reset":
        conversation_history.clear()
        print("Conversation history cleared")
        continue
    
    ai_response = ask_ai(user_input)
    print("AI: ", ai_response)

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# Stores conversation
conversation_history = []

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def ask_ai(prompt):
    global conversation_history

    # Add user's message
    conversation_history.append(prompt)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=conversation_history
    )

    ai_text = response.text

    # Store AI reply
    conversation_history.append(ai_text)

    return ai_text


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

    ai_reply = ask_ai(user_input)
    print("AI: ", ai_reply)

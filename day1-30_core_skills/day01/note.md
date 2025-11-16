# Day 01 - AI Chat Systems

## Objective
Learn how to build a simple interactive AI chat system using two different APIs:
1. Google Gemini API
2. OpenAI API

## What I Learned

### 1. Environment Setup
- Used `python-dotenv` to securely manage API keys.
- Stored keys in `.env` file:
```env
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key
```
- Loaded keys in Python using `load_dotenv()`.

### 2. Managing Conversation History
- Conversation history is stored in a list to maintain context across multiple messages.
- For Gemini:
```python
conversation_history = []  # simple list of strings
```
- For OpenAI:
```python
conversation_history = []  # list of dicts with role and content
conversation_history.append({"role": "user", "content": prompt})
conversation_history.append({"role": "assistant", "content": ai_message})
```

### 3. Using the APIs
#### Google Gemini API
- Created a client with `genai.Client(api_key=...)`.
- Sent conversation history as a list of strings.
- Received response using `client.models.generate_content`.

#### OpenAI API
- Used `requests` to send HTTP POST requests to `https://api.openai.com/v1/chat/completions`.
- Conversation history must be a list of messages in the format `{"role": "user"/"assistant", "content": "..."}`.
- Received response in JSON format and extracted AI message from `response.json()["choices"][0]["message"]["content"]`.

### 4. Chat Loop
- Implemented a continuous loop for user input.
- Special commands:
  - `/reset` → clears conversation history.
  - `exit` or `quit` → ends the chat.
- Example:
```python
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    elif user_input.lower() == "/reset":
        conversation_history.clear()
        continue
```

### 5. Error Handling
- For OpenAI API, wrapped the request in `try...except` to handle network/API errors:
```python
try:
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### 6. Key Takeaways
- Understanding conversation state is essential for multi-turn AI chat.
- APIs differ in how they accept conversation history:
  - Gemini → list of strings
  - OpenAI → list of dicts with `role` and `content`
- Environment variables are crucial for keeping API keys secure.
- Always handle errors when calling external APIs.
- Simple commands like `/reset` make the chat system more interactive.

## Next Steps
- Explore advanced conversation management (context trimming, summarization).
- Implement FastAPI.
- Learn Transformers to host a model on Google Colab.
- Use Grog to get a public URL that other apps can access.
- Build Python code to connect and interact with the hosted model.
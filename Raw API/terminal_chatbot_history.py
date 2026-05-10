import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
URL = "https://api.openai.com/v1/responses"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

# Keep the developer instruction once at the start.
history = [
    {
        "role": "developer",
        "content": "You are a helpful assistant. Be concise, accurate, and practical."
    }
]

MAX_MESSAGES = 20  # includes user + assistant turns, not the developer message


def trim_history(messages):
    """
    Keep the developer message and only the most recent turns.
    """
    if len(messages) <= MAX_MESSAGES + 1:
        return messages
    return [messages[0]] + messages[-MAX_MESSAGES:]


def chat(prompt: str) -> str:
    global history

    history.append({
        "role": "user",
        "content": prompt
    })

    history = trim_history(history)

    payload = {
        "model": "gpt-4.1-nano",
        "input": history,
        "store": False
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=60
    )
    response.raise_for_status()

    data = response.json()
    text = data["output"][0]["content"][0]["text"]

    history.append({
        "role": "assistant",
        "content": text
    })

    return text


if __name__ == "__main__":
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() == "exit":
            break

        try:
            answer = chat(user_text)
            print(f"Assistant: {answer}\n")
        except Exception as e:
            print(f"ERROR: {e}\n")
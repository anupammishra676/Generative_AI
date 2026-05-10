import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/responses"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

CHAT_HISTORY_FILE = "chat_history.json"

MAX_MESSAGES = 20


def load_history():

    if os.path.exists(CHAT_HISTORY_FILE):

        with open(CHAT_HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return [
        {
            "role": "developer",
            "content": (
                "You are a concise helpful assistant. "
                "Answer clearly and practically."
            )
        }
    ]


def save_history(history):

    with open(CHAT_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def trim_history(history):

    developer_message = history[0]

    recent_messages = history[-MAX_MESSAGES:]

    return [developer_message] + recent_messages


def stream_chat(history):

    payload = {
        "model": "gpt-4.1-nano",
        "stream": True,
        "store": False,
        "input": history
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        stream=True,
        timeout=60
    )

    response.raise_for_status()

    assistant_text = ""

    print("\nAssistant:\n")

    for line in response.iter_lines():

        if line:

            decoded_line = line.decode("utf-8")

            if decoded_line.startswith("data: "):

                data_str = decoded_line[len("data: "):]

                if data_str == "[DONE]":
                    break

                try:

                    data = json.loads(data_str)

                    event_type = data.get("type")

                    if event_type == "response.output_text.delta":

                        delta = data.get("delta", "")

                        assistant_text += delta

                        print(delta, end="", flush=True)

                except json.JSONDecodeError:
                    pass

    print("\n")

    return assistant_text


def main():

    print("=== Persistent RAW API Chatbot ===")
    print("Type 'exit' to quit.\n")

    history = load_history()

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nConversation saved.")
            break

        history.append({
            "role": "user",
            "content": user_input
        })

        history = trim_history(history)

        try:

            assistant_reply = stream_chat(history)

            history.append({
                "role": "assistant",
                "content": assistant_reply
            })

            save_history(history)

        except Exception as e:

            print(f"\nERROR: {str(e)}")


if __name__ == "__main__":
    main()


# Storing raw history is terrible. Real time application uses below methods
# Instead they use:

# summarization
# semantic memory
# retrieval memory
# episodic memory
# vector search
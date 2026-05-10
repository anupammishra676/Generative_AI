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


def stream_chat(prompt, previous_response_id=None):

    payload = {
        "model": "gpt-4.1-nano",
        "stream": True,
        "input": [
            {
                "role": "developer",
                "content": (
                    "You are a concise helpful AI assistant. "
                    "Keep answers clear and practical."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    if previous_response_id:
        payload["previous_response_id"] = previous_response_id

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        stream=True,
        timeout=60
    )

    response.raise_for_status()

    full_text = ""
    response_id = None

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

                    # streaming token
                    if event_type == "response.output_text.delta":

                        delta = data.get("delta", "")

                        full_text += delta

                        print(delta, end="", flush=True)

                    # completed response event
                    elif event_type == "response.completed":

                        response_obj = data.get("response", {})

                        response_id = response_obj.get("id")

                except json.JSONDecodeError:
                    pass

    print("\n")

    return full_text, response_id


def main():

    print("=== RAW API TERMINAL CHATBOT ===")
    print("Type 'exit' to quit.\n")

    previous_response_id = None

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nGoodbye.")
            break

        try:

            _, previous_response_id = stream_chat(
                user_input,
                previous_response_id
            )

        except Exception as e:
            print(f"\nERROR: {str(e)}")


if __name__ == "__main__":
    main()
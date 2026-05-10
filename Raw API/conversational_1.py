import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

URL = "https://api.openai.com/v1/responses"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}


def chat(prompt, previous_response_id=None):

    payload = {
        "model": "gpt-4.1-nano",
        "input": [
            {
                "role": "developer",
                "content": "You are a helpful AI assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    # only include if available
    if previous_response_id:
        payload["previous_response_id"] = previous_response_id

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    text = data["output"][0]["content"][0]["text"]

    response_id = data["id"]

    return text, response_id


# First message
reply1, resp_id = chat("My name is Anupam.")

print("\nAssistant:", reply1)
print("Response ID:", resp_id)

# Second message
reply2, resp_id2 = chat(
    "What is my name?",
    previous_response_id=resp_id
)

print("\nAssistant:", reply2)
print("Response ID:", resp_id2)
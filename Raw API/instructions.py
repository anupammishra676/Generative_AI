import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def call_openai(prompt: str) -> str:
    if not api_key:
        raise ValueError("OPENAI_API_KEY is missing")

    url = "https://api.openai.com/v1/responses"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.strip()}",
    }

    payload = {
        "model": "gpt-4.1",
        "input": [
            {
                "role": "developer",
                "content": "You are a concise assistant. Answer in one short paragraph."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()

    return data["output"][0]["content"][0]["text"]


text = call_openai("Explain Gen AI in simple words.")
print(text)
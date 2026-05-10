import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/responses"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
payload = {
    "model": "gpt-4.1",
    "input": "Say hello in one short sentence."
}

response = requests.post(url, headers=headers, json=payload, timeout=60)
response.raise_for_status()

data = response.json()

print("Response ID:", data["id"])
print("Status:", data["status"])
print("Text:", data["output"][0]["content"][0]["text"])
print("Status:", data["output"][0]["status"])
print(json.dumps(data, indent= 2))
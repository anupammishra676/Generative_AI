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


payload = {
    "model": "gpt-4.1-nano",
    "input": "Explain streaming in simple words.",
    "stream": True
}


response = requests.post(
    URL,
    headers=HEADERS,
    json=payload,
    stream=True
)

response.raise_for_status()

print("\nAssistant:\n")

for line in response.iter_lines():

    if line:

        decoded_line = line.decode("utf-8")

        # SSE lines start with "data: "
        if decoded_line.startswith("data: "):

            data_str = decoded_line[len("data: "):]

            # stream completion signal
            if data_str == "[DONE]":
                break

            try:
                data = json.loads(data_str)

                event_type = data.get("type")

                # incremental text token
                if event_type == "response.output_text.delta":

                    delta = data.get("delta", "")

                    print(delta, end="", flush=True)

            except json.JSONDecodeError:
                pass
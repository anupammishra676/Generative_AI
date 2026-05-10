import os
import requests
from dotenv import load_dotenv


class OpenAIAPIError(Exception):
    pass


def call_openai(prompt: str, model: str = "gpt-4.1") -> str:
    load_dotenv()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise OpenAIAPIError("OPENAI_API_KEY is missing")

    url = "https://api.openai.com/v1/responses"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.strip()}",
    }
    payload = {
        "model": model,
        "input": prompt,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise OpenAIAPIError(
            f"HTTP error {response.status_code}: {response.text}"
        ) from e
    except requests.exceptions.RequestException as e:
        raise OpenAIAPIError(f"Network/request error: {str(e)}") from e

    data = response.json()

    try:
        return data["output"][0]["content"][0]["text"]  #get the output from json
    except (KeyError, IndexError, TypeError) as e:
        raise OpenAIAPIError(f"Unexpected response format: {data}") from e


if __name__ == "__main__":
    text = call_openai("Say hello in one short sentence.")
    print(text)
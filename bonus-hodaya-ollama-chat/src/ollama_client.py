import requests

from src.config import OLLAMA_URL, OLLAMA_MODEL, APP_API_KEY, REQUEST_TIMEOUT


class OllamaClient:
    """
    Handles direct API communication with the local Ollama server.
    The GUI does not use any web interface. It sends HTTP API requests directly.
    """

    def __init__(self):
        self.url = OLLAMA_URL
        self.model = OLLAMA_MODEL
        self.api_key = APP_API_KEY

    def chat(self, messages):
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        }

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }

        try:
            response = requests.post(
                self.url,
                json=payload,
                headers=headers,
                timeout=REQUEST_TIMEOUT
            )
            response.raise_for_status()
            data = response.json()

            if "message" in data and "content" in data["message"]:
                return data["message"]["content"].strip()

            if "response" in data:
                return data["response"].strip()

            return "No response content was returned from the model."

        except requests.exceptions.RequestException as error:
            return f"API error: {error}"

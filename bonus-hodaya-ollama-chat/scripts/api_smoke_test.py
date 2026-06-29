import requests
from dotenv import load_dotenv
import os

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "smollm:135m")
APP_API_KEY = os.getenv("APP_API_KEY", "local-dev-key")

headers = {
    "Content-Type": "application/json",
    "X-API-Key": APP_API_KEY
}

payload = {
    "model": OLLAMA_MODEL,
    "messages": [
        {
            "role": "user",
            "content": "Reply with one short sentence confirming the API works."
        }
    ],
    "stream": False
}

print("Testing local Ollama API...")
print(f"URL: {OLLAMA_URL}")
print(f"Model: {OLLAMA_MODEL}")

response = requests.post(
    OLLAMA_URL,
    json=payload,
    headers=headers,
    timeout=120
)

response.raise_for_status()
data = response.json()

print("API test passed.")
print("Model response:")
print(data.get("message", {}).get("content", data))

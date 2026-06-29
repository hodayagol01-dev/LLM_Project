from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(ENV_PATH)

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "smollm:135m")
APP_API_KEY = os.getenv("APP_API_KEY", "local-dev-key")
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "120"))

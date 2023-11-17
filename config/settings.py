import os
from pathlib import Path

from dotenv import load_dotenv

# GENERAL
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables
load_dotenv(os.path.join(BASE_DIR, ".env"))

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

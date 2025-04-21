import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")
UPLOAD_URL = os.getenv("UPLOAD_URL")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
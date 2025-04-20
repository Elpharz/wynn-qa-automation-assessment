import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "https://jsonplaceholder.typicode.com")
UPLOAD_URL = os.getenv("UPLOAD_URL")
HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
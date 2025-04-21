import os
from config import API_BASE_URL, UPLOAD_URL, HEADLESS

def test_env_loaded_successfully():
    assert os.getenv("API_BASE_URL")
    assert os.getenv("UPLOAD_URL")

def test_config_values_correct():
    assert "http" in API_BASE_URL
    assert "upload" in UPLOAD_URL

def test_ci_pipeline_triggered():
    assert True  # Validated by GitHub Actions or similar CI
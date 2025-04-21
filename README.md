<<<<<<< HEAD
# wynn-qa-automation-assessment
Automation framework using Playwright (Python) for UI tests and Pytest for API testing. Includes Allure reporting, environment configs, and a clean, scalable architecture. Built for the Wynn Al Marjan QA Engineer assessment
=======
# 🧪 QA Automation Suite – Wynn Al Marjan Island

Automated test suite using Python + Playwright for both UI and API functionality validation.

## Features
- ✅ UI tests for file upload page
- ✅ API tests for /posts endpoint
- ✅ Allure reports
- ✅ CI integration (GitHub Actions)
- ✅ Secure config with `.env`

## Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

## Running Tests
```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
```
>>>>>>> af1cab9 (Initial commit: project structure, virtualenv, and config setup)

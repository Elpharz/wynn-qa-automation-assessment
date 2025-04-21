# 🏗️ Test Framework Architecture

## Technologies Used
- Python 3.10
- Pytest for test runner and reporting
- Playwright for browser automation
- Allure for reporting
- GitHub Actions for CI/CD
- .env / python-dotenv for environment handling

## Structure Overview
```
wynn_qa_assessment/
├── tests/
│   ├── ui/pages/           # Page Object Model
│   ├── api/clients/        # HTTP clients and helpers
│   ├── performance/        # Performance scripts (placeholder)
│   └── test_data/          # Files and resources
├── docs/                   # Strategy & architecture
├── reports/                # Test reports
├── .github/workflows/      # CI/CD setup
└── config.py, .env         # Config
```

## Design Patterns
- Page Object Model for UI
- Modular test clients for API
- Parametrization for multiple test variations
- Environment separation via .env and config.py

## Scalability
Supports easy addition of tests, CI workflows, and reporting integrations.

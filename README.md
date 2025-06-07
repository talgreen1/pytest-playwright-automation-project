# pytest-playwright-automation-project

## Introduction

This is a demo automation project for both UI and API testing. It showcases best practices for structuring and running automated tests using modern Python tools. The project demonstrates:
- UI automation using Playwright
- API testing with requests
- Rich test reporting with Allure

## Technology Stack

- **Python 3.8+**: Programming language for all tests and utilities
- **Pytest**: Test runner and framework
- **Playwright**: UI browser automation
- **Allure**: Test reporting and visualization
- **requests**: (for API tests)

## Prerequisites

1. **Install Python 3.8+** and ensure `pip` is available.
2. **Install project dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Install Allure CLI:**
   - **Windows (using Scoop):**
     ```powershell
     Set-ExecutionPolicy RemoteSigned -scope CurrentUser
     irm get.scoop.sh | iex
     scoop install allure
     ```
   - **macOS (using Homebrew):**
     ```bash
     brew install allure
     ```
   - For other OS or manual installation, see https://docs.qameta.io/allure/ for instructions.

## How to Run Tests

1. (Optional) Activate your virtual environment:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
2. Run the tests with Allure reporting (default is headed mode):
   ```powershell
   pytest --alluredir=allure-results
   ```
   By default, tests run in headed mode (browser UI visible).

3. To run tests in headless mode (browser UI hidden):
   ```powershell
   pytest --alluredir=allure-results --headless true
   ```
   Or set the environment variable before running:
   ```powershell
   $env:HEADLESS="true"
   pytest --alluredir=allure-results
   ```

4. To view the Allure report:
   ```powershell
   allure serve allure-results
   ```

## Project Structure

```
pytest-playwright-automation-project/
├── pages/                # Page Object Model classes
│   ├── __init__.py
│   └── config.py
├── tests/                # Test cases (UI & API)
│   ├── api/              # API test cases and utilities
│   └── ui/               # UI test cases (if present)
├── conftest.py           # Pytest fixtures and configuration
├── test_settings.py      # Centralized test settings
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── allure-results/       # Allure test result files
└── __pycache__/          # Python bytecode cache
```

## Example

A single login test for https://www.saucedemo.com/v1/ is implemented in `tests/test_login.py`.


TODOS
# Todo:  
- capture video
- move steps definitions to step implementations
- 
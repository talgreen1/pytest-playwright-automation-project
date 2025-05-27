# pytest-playwright-automation-project

# Pytest + Playwright + Allure Example

## Prerequisites

1. Install Python 3.8+ and pip if not already installed.
2. Install project dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
3. Install Allure CLI:
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

## How to run tests

1. (Optional) Activate your virtual environment:
   
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Run the tests with Allure reporting:
   
   ```powershell
   pytest --alluredir=allure-results
   ```

3. To view the Allure report:
   
   ```powershell
   allure serve allure-results
   ```

## Project Structure

- `pages/` - Page Object Model classes
- `tests/` - Test cases
- `conftest.py` - Pytest fixtures

## Example

A single login test for https://www.saucedemo.com/v1/ is implemented in `tests/test_login.py`.

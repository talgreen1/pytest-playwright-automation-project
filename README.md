# pytest-playwright-automation-project

# Pytest + Playwright + Allure Example

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

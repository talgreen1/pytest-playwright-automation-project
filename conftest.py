import pytest
from playwright.sync_api import sync_playwright
import os
from config import URL
from test_settings import HEADLESS, TIMEOUT, SLOWMO
import glob

def get_cli_options(request):
    """Return CLI options for headless and slowmo as a dict."""
    headless_cli = request.config.getoption('--headless')
    slowmo_cli = request.config.getoption('--slowmo')
    return {
        'headless': headless_cli,
        'slowmo': slowmo_cli
    }

def get_headless_option(cli_options):
    # Priority: pytest CLI > env var > test_settings.py default
    headless_cli = cli_options['headless']
    if headless_cli is not None:
        return headless_cli.lower() in ['1', 'true', 'yes']
    headless_env = os.getenv('HEADLESS')
    if headless_env is not None:
        return headless_env.lower() in ['1', 'true', 'yes']
    return HEADLESS

def get_slowmo_option(cli_options):
    slowmo_cli = cli_options['slowmo']
    if slowmo_cli is not None:
        try:
            return int(slowmo_cli)
        except ValueError:
            pass
    slowmo_env = os.getenv('SLOWMO')
    if slowmo_env is not None:
        try:
            return int(slowmo_env)
        except ValueError:
            pass
    return SLOWMO

# Use HEADLESS and SLOWMO from test_settings.py as default

def pytest_addoption(parser):
    parser.addoption('--headless', action='store', default=None, help='Run browser in headless mode (true/false)')
    parser.addoption('--slowmo', action='store', default=None, help='Slow down Playwright operations by the specified ms')
    # Example for future: parser.addoption('--timeout', action='store', default=None, help='Set browser timeout (ms)')

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    cli_options = get_cli_options(request)
    headless = get_headless_option(cli_options)
    slowmo = get_slowmo_option(cli_options)
    browser = playwright_instance.chromium.launch(headless=headless, slow_mo=slowmo)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def pytest_sessionstart(session):
    """Delete all JSON files in allure-results before test session starts."""
    results_dir = os.path.join(os.path.dirname(__file__), '../allure-results')
    json_files = glob.glob(os.path.join(results_dir, '*.json'))
    for f in json_files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Could not delete {f}: {e}")

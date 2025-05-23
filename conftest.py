import pytest
from playwright.sync_api import sync_playwright
import os
from pages.config import URL
from test_settings import HEADLESS, TIMEOUT, SLOWMO

# Use HEADLESS and SLOWMO from test_settings.py as default

def get_headless_option():
    # Priority: pytest CLI > env var > test_settings.py default
    headless_env = os.getenv('HEADLESS')
    if headless_env is not None:
        return headless_env.lower() in ['1', 'true', 'yes']
    return HEADLESS

def get_slowmo_option(request):
    slowmo_cli = request.config.getoption('--slowmo')
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
    headless_cli = request.config.getoption('--headless')
    if headless_cli is not None:
        headless = headless_cli.lower() in ['1', 'true', 'yes']
    else:
        headless = get_headless_option()
    slowmo = get_slowmo_option(request)
    browser = playwright_instance.chromium.launch(headless=headless, slow_mo=slowmo)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

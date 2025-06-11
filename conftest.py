import pytest
from playwright.sync_api import sync_playwright
import os
from config import URL
from test_settings import HEADLESS, SLOWMO
import glob
import allure

def get_cli_options(request):
    """Return CLI options for headless and slowmo as a dict."""
    # Only get CLI options if they exist, otherwise use None
    try:
        headless_cli = request.config.getoption('--headless')
    except (ValueError, AttributeError):
        headless_cli = None
    return {
        'headless': headless_cli,
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

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance, request):
    cli_options = get_cli_options(request)
    headless = get_headless_option(cli_options)
    browser = playwright_instance.chromium.launch(headless=headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser, request, tmp_path):
    # Enable video recording in the context
    context = browser.new_context(
        record_video_dir=str(tmp_path)
    )
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IN THE FIXTURE")
    import pdb; pdb.set_trace()
    breakpoint()
    page = context.new_page()
    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield page
    # Stop tracing and save
    trace_path = str(tmp_path / "trace.zip")
    context.tracing.stop(path=trace_path)
    # Ensure the trace file is flushed to disk before closing context
    page.close()
    context.close()
    # Save and attach video and trace to Allure
    try:
        video_path = page.video.path()
        if video_path and os.path.exists(video_path):
            allure.attach.file(video_path, name="Test Video", attachment_type=allure.attachment_type.MP4)
        if os.path.exists(trace_path):
            with open(trace_path, "rb") as f:
                allure.attach(f.read(), name="Playwright Trace", attachment_type=allure.attachment_type.BINARY)
    except Exception as e:
        pass

def pytest_sessionstart(session):
    """Delete all JSON files in allure-results before test session starts."""
    results_dir = os.path.join(os.path.dirname(__file__), '../allure-results')
    json_files = glob.glob(os.path.join(results_dir, '*.json'))
    for f in json_files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Could not delete {f}: {e}")

def pytest_addoption(parser):
    parser.addoption('--headless', action='store', default=None, help='Run browser in headless mode (true/false)')

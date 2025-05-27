import pytest
from pages.login_page import LoginPage
import allure
from pages.config import USERNAME, PASSWORD

@allure.feature("Login")
@allure.story("Valid Login")
def test_login_success(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_logged_in(), "Login failed, Products page not visible."

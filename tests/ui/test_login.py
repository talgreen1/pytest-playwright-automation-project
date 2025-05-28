import pytest
from pages.login_page import LoginPage
import allure
from pages.config import USERNAME, PASSWORD

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Successful login with valid credentials")
@allure.description("This test verifies that a user can log in with valid credentials and see the Products page.")
def test_login_success(page):
    with allure.step("Start login test"):  # Top-level test step
        login_page = LoginPage(page)
        login_page.load()
        login_page.login(USERNAME, PASSWORD)
        with allure.step("Verify user is logged in"):
            assert login_page.is_logged_in(), "Login failed, Products page not visible."
        with allure.step("Verify there are exactly 6 product listings"):
            product_count = page.locator('.inventory_item').count()
            assert product_count == 6, f"Expected 6 product listings, found {product_count}."

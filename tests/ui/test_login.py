import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import allure
from config import USERNAME, PASSWORD

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Successful login with valid credentials")
@allure.description("Ensures that logging in with valid credentials displays the Products page and exactly 6 product listings.")
def test_login_success(page):
    with allure.step("Start login test"):  # Top-level test step
        login_page = LoginPage(page)
        login_page.load()
        login_page.login(USERNAME, PASSWORD)
        with allure.step("Verify user is logged in"):
            assert login_page.is_logged_in(), "Login failed, Products page not visible."
        with allure.step("Verify there are exactly 6 product listings"):
            products_page = ProductsPage(page)
            product_count = products_page.get_product_count()
            assert product_count == 6, f"Expected 6 product listings, found {product_count}."

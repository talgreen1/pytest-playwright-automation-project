import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import allure
from config import USERNAME, PASSWORD
from playwright.sync_api import expect
from test_params import EXPECTED_PRODUCT_COUNT

@allure.feature("Login")
@allure.story("Valid Login")
@allure.title("Successful login with valid credentials")
@allure.description("Ensures that logging in with valid credentials displays the Products page and exactly 6 product listings.")
@allure.label("category", "UI")
def test_login_success(page):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IN THE TEST")
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    login_page.is_logged_in()
    with allure.step(f"Verify there are exactly {EXPECTED_PRODUCT_COUNT} product listings"):
        products_page = ProductsPage(page)
        product_count = products_page.get_product_count()
        assert product_count == EXPECTED_PRODUCT_COUNT, f"Expected {EXPECTED_PRODUCT_COUNT} product listings, found {product_count}."

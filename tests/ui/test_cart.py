import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import allure
from config import USERNAME, PASSWORD

@allure.feature("Cart")
@allure.story("Add first item to cart and check cart badge")
@allure.title("Add first product to cart and verify cart badge")
@allure.description("This test logs in, adds the first product to the cart, and verifies that the cart badge shows '1'.")
@allure.label("category", "UI")
def test_add_first_item_to_cart(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    login_page.is_logged_in()
    products_page = ProductsPage(page)
    products_page.add_first_item_to_cart()
    products_page.expect_cart_count(1)
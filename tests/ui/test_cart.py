import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import allure
from config import USERNAME, PASSWORD

@allure.feature("Cart")
@allure.story("Add first item to cart and check cart badge")
@allure.title("Add first product to cart and verify cart badge")
@allure.description("This test logs in, adds the first product to the cart, and verifies that the cart badge shows '1'.")
def test_add_first_item_to_cart(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)
    assert login_page.is_logged_in(), "Login failed, Products page not visible."
    products_page = ProductsPage(page)
    products_page.add_first_item_to_cart()
    assert products_page.get_cart_count() == 1, "Cart badge does not show '1' after adding item."
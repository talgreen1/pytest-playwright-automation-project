import pytest
from pages.login_page import LoginPage
import allure
from pages.products_page import ProductsPage

@allure.feature("Login")
@allure.story("Valid Login")
def test_login_success(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in(), "Login failed, Products page not visible."

@allure.feature("Cart")
@allure.story("Add first item to cart and check cart badge")
def test_add_first_item_to_cart(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in(), "Login failed, Products page not visible."
    products_page = ProductsPage(page)
    products_page.add_first_item_to_cart()
    assert products_page.get_cart_count() == 1, "Cart badge does not show '1' after adding item."

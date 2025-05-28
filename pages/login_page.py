from playwright.sync_api import Page
from .config import URL
import allure

class LoginPage:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PRODUCTS_TITLE = ".product_label"

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        with allure.step("Navigate to login page"):
            self.page.goto(URL)

    @allure.step("Login as user: {username}")
    def login(self, username: str, password: str):
        with allure.step("Fill username"):
            self.page.fill(self.USERNAME_INPUT, username)
        with allure.step("Fill password"):
            self.page.fill(self.PASSWORD_INPUT, password)
        with allure.step("Click login button"):
            self.page.click(self.LOGIN_BUTTON)

    @allure.step("Check if user is logged in")
    def is_logged_in(self) -> bool:
        return self.page.is_visible(self.PRODUCTS_TITLE)

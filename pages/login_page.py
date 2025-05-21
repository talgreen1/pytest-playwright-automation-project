from playwright.sync_api import Page

class LoginPage:
    URL = "https://www.saucedemo.com/v1/"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PRODUCTS_TITLE = ".product_label"

    def __init__(self, page: Page):
        self.page = page

    def load(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def is_logged_in(self) -> bool:
        return self.page.is_visible(self.PRODUCTS_TITLE)

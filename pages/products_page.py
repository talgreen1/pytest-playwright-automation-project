from playwright.sync_api import Page

class ProductsPage:
    FIRST_ADD_TO_CART_BUTTON = "button.btn_primary.btn_inventory"  # First 'Add to cart' button
    CART_BADGE = ".shopping_cart_badge"  # Cart icon badge

    def __init__(self, page: Page):
        self.page = page

    def add_first_item_to_cart(self):
        self.page.click(self.FIRST_ADD_TO_CART_BUTTON)

    def get_cart_count(self) -> int:
        if self.page.is_visible(self.CART_BADGE):
            return int(self.page.inner_text(self.CART_BADGE))
        return 0

from playwright.sync_api import Page, expect
import allure

class ProductsPage:
    FIRST_ADD_TO_CART_BUTTON = "button.btn_primary.btn_inventory"  # First 'Add to cart' button
    CART_BADGE = ".shopping_cart_badge"  # Cart icon badge
    PRODUCT_ITEM = ".inventory_item"

    def __init__(self, page: Page):
        self.page = page
        self.product_item_locator = self.page.locator(self.PRODUCT_ITEM)

    @allure.step("Add first item to cart")
    def add_first_item_to_cart(self):
        self.page.click(self.FIRST_ADD_TO_CART_BUTTON)
    
    @allure.step("Expect cart count to be {count}")
    def expect_cart_count(self, count: int):
        expect(self.page.locator(self.CART_BADGE)).to_have_text(str(count))

    def get_product_count(self) -> int:
        return self.page.locator(self.PRODUCT_ITEM).count()
    
    def expect_product_count(self, count) -> int:
        expect (self.page.locator(self.PRODUCT_ITEM)).to_have_count(count)

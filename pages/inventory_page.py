from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"

    def __init__(self, driver):
        super().__init__(driver)

    ADD_BACKPACK_BUTTON = (
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )

    REMOVE_BACKPACK_BUTTON = (
        By.ID,
        "remove-sauce-labs-backpack"
    )

    CART_ICON = (
        By.CLASS_NAME,
        "shopping_cart_link"
    )

    CART_BADGE = (
        By.CLASS_NAME,
        "shopping_cart_badge"
    )

    SORT_DROPDOWN = (
        By.CLASS_NAME,
        "product_sort_container"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    def open(self):
        self.open_url(self.URL)

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BUTTON)

    def remove_backpack_from_cart(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_cart_badge_count(self):

        badges = self.driver.find_elements(
            *self.CART_BADGE
        )

        if not badges:
            return 0

        return int(badges[0].text)

    def sort_products_by_price_low_to_high(self):

        dropdown = Select(
            self.driver.find_element(
                *self.SORT_DROPDOWN
            )
        )

        dropdown.select_by_value("lohi")

    def get_product_prices(self):

        price_elements = self.driver.find_elements(
            *self.PRODUCT_PRICES
        )

        return [
            float(price.text.replace("$", ""))
            for price in price_elements
        ]
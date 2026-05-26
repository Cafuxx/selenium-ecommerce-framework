from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME_INPUT = (
        By.ID,
        "first-name"
    )

    LAST_NAME_INPUT = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE_INPUT = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    CART_ITEM_NAME = (
        By.CLASS_NAME,
        "inventory_item_name"
    )
    
    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    def fill_checkout_form(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.write(self.FIRST_NAME_INPUT, first_name)
        self.write(self.LAST_NAME_INPUT, last_name)
        self.write(self.POSTAL_CODE_INPUT, postal_code)

    def click_continue(self):

        self.click(self.CONTINUE_BUTTON)
        
    def get_error_message(self):
        
        return self.get_text(
            self.ERROR_MESSAGE
        )

    def get_first_item_name(self):

        return self.get_text(
            *self.CART_ITEM_NAME)
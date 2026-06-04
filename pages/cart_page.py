from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        
    cart_item = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "[id^='remove-']")
    
    def get_first_item_name(self):
        return self.get_text(self.cart_item)
        
    def click_checkout(self):
        self.click(self.checkout_button)
        
    def remove_backpack_from_cart(self):
        self.click(self.remove_button)

    def get_cart_items_count(self):
        return len(self.find_all(self.cart_item))
    
    def remove_product_from_cart(self, product_name):
        product_id = (
            product_name.lower()
            .replace(" ", "-")
        )
        
        remove_button = (By.ID, f"remove-{product_id}")
        
        self.click(remove_button)
        
    def remove_all_products(self):
        """Remove all products from cart one by one"""
        wait = WebDriverWait(self.driver, 10)
        while True:
            try:
                # Find all remove buttons
                remove_buttons = self.driver.find_elements(*self.REMOVE_BUTTONS)
                if not remove_buttons:
                    break
                # Click first remove button
                self.driver.execute_script("arguments[0].scrollIntoView(true);", remove_buttons[0])
                remove_buttons[0].click()
                # Wait for DOM to update
                wait.until(EC.staleness_of(remove_buttons[0]))
            except:
                break
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
        
    cart_item = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-backpack")
    checkout_button = (By.ID, "checkout")
    
    def get_first_item_name(self):
        return self.get_text(self.cart_item)
        
    def click_checkout(self):
        self.click(self.checkout_button)
        
    def remove_backpack_from_cart(self):
        self.click(self.remove_button)

    def get_cart_items_count(self):
        return len(self.driver.find_all(self.CART_ITEM))
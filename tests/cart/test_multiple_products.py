import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage

from utils.test_data import PRODUCTS

@pytest.mark.regression
def test_add_multiple_products_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.open()
    
    for i, product in enumerate(PRODUCTS, 1):
        inventory_page.add_product_to_cart(product)
    
    inventory_page.go_to_cart()
    print("URL:", driver.current_url)
    assert cart_page.get_cart_items_count() == len(PRODUCTS)

def get_cart_items_count(self):
    print("Current URL:", self.driver.current_url)
    return len(self.find_all(self.cart_item))
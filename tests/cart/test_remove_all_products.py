import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.test_data import PRODUCTS

@pytest.mark.regression
def test_remove_all_products_from_cart(driver):
    

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    inventory_page.open()
    
    for product in PRODUCTS:
        inventory_page.add_product_to_cart(product)
        
    inventory_page.go_to_cart()
    
    cart_page.remove_all_products()
    
    assert cart_page.get_cart_items_count() == 0
import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.test_data import PRODUCTS

@pytest.mark.regression
def test_add_multiple_products_to_cart(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    inventory_page.open()
    
    for product in PRODUCTS:
        inventory_page.add_product_to_cart(product)
        inventory_page.go_to_cart()
        assert (cart_page.get_cart_items_count() == len(PRODUCTS))
import pytest

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

from utils.test_data import(
    INVALID_CHECKOUT_DATA
)

@pytest.mark.regression
@pytest.mark.parametrize("first_name, last_name, postal_code, error_message", INVALID_CHECKOUT_DATA)
def test_checkout_validation(driver, first_name, last_name, postal_code, error_message):
    # Implementation for checkout validation test
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    inventory_page.open()
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    cart_page.click_checkout()
    checkout_page.fill_checkout_form(first_name, last_name, postal_code)
    checkout_page.click_continue()
    
    assert (checkout_page.get_error_message() == error_message)
    

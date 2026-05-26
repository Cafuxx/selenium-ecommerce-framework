import pytest

from pages.login_page import LoginPage

from utils.test_data import INVALID_LOGIN_DATA

@pytest.mark.regression
@pytest.mark.parametrize("username, password, error_message", INVALID_LOGIN_DATA)

def test_negative_login(driver, username, password, error_message):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    
    assert (login_page.get_error_message() == error_message)
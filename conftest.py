import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"screenshots/{item.name}.png")
            
@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return driver


def _clear_browser_storage(driver):
    # Helper to clear all browser storage
    try:
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        driver.delete_all_cookies()
    except:
        pass

@pytest.fixture(scope="function", autouse=True)
def cleanup_after_test(driver, request):
    # Cleanup before and after each test to reset cart
    # Before test - navigate to login page and clear cookies
    driver.get("https://www.saucedemo.com/")
    driver.delete_all_cookies()
    
    yield
    
    # After test - logout and clear storage
    try:
        login_page = LoginPage(driver)
        if login_page.is_element_present(login_page.MENU_BUTTON):
            login_page.logout()
    except:
        pass
    
    try:
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
        driver.delete_all_cookies()
    except:
        pass

@pytest.fixture(scope="function")
def driver():
    # Set Up
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    yield driver
    
    # Tear Down
    driver.quit()
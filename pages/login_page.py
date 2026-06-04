from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    
    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
        
    def open(self):
        self.open_url(self.URL)
        
    def login(self, username, password):
        self.write(self.USERNAME_INPUT, username)
        self.write(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
            
    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
    
    def logout(self):
        try:
            self.click(self.MENU_BUTTON)
            self.click(self.LOGOUT_LINK)
        except:
            pass 
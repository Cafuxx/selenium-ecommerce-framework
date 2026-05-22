from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage: 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        
    def open_url(self, url):
        self.driver.get(url)
        
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def find_all(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def write(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
    def get_text(self, locator):
        return self.find(locator).text
    
    def is_element_present(self, locator):
        
        return len(self.driver.find_elements(*locator)) > 0
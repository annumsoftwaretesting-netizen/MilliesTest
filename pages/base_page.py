from selenium.common.exceptions import (
    StaleElementReferenceException,
    TimeoutException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
 
 
class BasePage:
 
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
 
    def wait_for_page_load(self):
        self.wait.until(
            lambda driver:
            driver.execute_script(
                "return document.readyState"
            ) == "complete"
        )
 
    def click(self, locator):
        try:
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()
        except StaleElementReferenceException:
            # page re-rendered between the wait and the click;
            # re-locate the element once and retry
            self.wait.until(
                EC.element_to_be_clickable(locator)
            ).click()
 
    def js_click(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
 
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
 
    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
 
        element.clear()
        element.send_keys(text)
 
    def press_enter(self, locator):
        self.driver.find_element(
            *locator
        ).send_keys(Keys.ENTER)
 
    def get_text(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        ).text
 
    def is_visible(self, locator):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except TimeoutException:
            return False
 
    def scroll_into_view(self, locator):
        element = self.wait.until(
            EC.presence_of_element_located(locator)
        )
 
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            element
        )
 
    def take_screenshot(self, name):
        self.driver.save_screenshot(
            f"screenshots/{name}.png"
        )
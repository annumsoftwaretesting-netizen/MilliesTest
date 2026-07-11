from selenium.webdriver.common.by import By
 
from pages.base_page import BasePage
 
 
class CheckoutPage(BasePage):
 
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    ADDRESS = (By.ID, "address")
    POSTCODE = (By.ID, "postcode")
 
    CONTINUE = (
        By.CSS_SELECTOR,
        ".continue-button"
    )
 
    def enter_details(
        self,
        first,
        last,
        address,
        postcode
    ):
 
        self.enter_text(
            self.FIRST_NAME,
            first
        )
 
        self.enter_text(
            self.LAST_NAME,
            last
        )
 
        self.enter_text(
            self.ADDRESS,
            address
        )
 
        self.enter_text(
            self.POSTCODE,
            postcode
        )
 
        self.click(
            self.CONTINUE
        )
 
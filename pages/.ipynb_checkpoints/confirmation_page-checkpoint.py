from selenium.webdriver.common.by import By
 
from pages.base_page import BasePage
 
 
class ConfirmationPage(BasePage):
 
    ORDER_NUMBER = (
        By.CSS_SELECTOR,
        ".order-number"
    )
 
    def get_order_number(self):
 
        return self.get_text(
            self.ORDER_NUMBER
        )
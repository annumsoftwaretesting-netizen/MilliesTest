from pages.base_page import BasePage
from selenium.webdriver.common.by import By
 
 
class BasketPage(BasePage):
 
    BASKET_COUNT = (
        By.CSS_SELECTOR,
        ".basket-count"
    )
 
    def get_basket_count(self):
 
        return self.get_text(
            self.BASKET_COUNT
        )
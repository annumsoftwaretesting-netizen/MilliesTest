from selenium.webdriver.common.by import By
 
from pages.base_page import BasePage
 
 
class PaymentPage(BasePage):
 
    CARD_NUMBER = (
        By.ID,
        "cardNumber"
    )
 
    EXPIRY = (
        By.ID,
        "expiry"
    )
 
    CVV = (
        By.ID,
        "cvv"
    )
 
    PAY_BUTTON = (
        By.ID,
        "pay-now"
    )
 
    def pay(
        self,
        card,
        expiry,
        cvv
    ):
 
        self.enter_text(
            self.CARD_NUMBER,
            card
        )
 
        self.enter_text(
            self.EXPIRY,
            expiry
        )
 
        self.enter_text(
            self.CVV,
            cvv
        )
 
        self.click(
            self.PAY_BUTTON
        )
from pages.base_page import BasePage
from locators.payment_locators import PaymentLocators


class PaymentPage(BasePage):

    def pay(
        self,
        card,
        expiry,
        cvv
    ):

        self.enter_text(
            PaymentLocators.CARD_NUMBER,
            card
        )

        self.enter_text(
            PaymentLocators.EXPIRY,
            expiry
        )

        self.enter_text(
            PaymentLocators.CVV,
            cvv
        )

        self.click(
            PaymentLocators.PAY_BUTTON
        )

from pages.base_page import BasePage
from locators.confirmation_locators import ConfirmationLocators


class ConfirmationPage(BasePage):

    def get_order_number(self):

        return self.get_text(
            ConfirmationLocators.ORDER_NUMBER
        )

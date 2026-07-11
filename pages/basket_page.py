from pages.base_page import BasePage
from locators.basket_locators import BasketLocators


class BasketPage(BasePage):

    def get_basket_count(self):

        return self.get_text(
            BasketLocators.BASKET_COUNT
        )

    def checkout(self):

        self.click(
            BasketLocators.CHECKOUT_BUTTON
        )

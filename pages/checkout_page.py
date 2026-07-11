from pages.base_page import BasePage
from locators.checkout_locators import CheckoutLocators


class CheckoutPage(BasePage):

    def enter_details(
        self,
        first,
        last,
        address,
        postcode
    ):

        self.enter_text(
            CheckoutLocators.FIRST_NAME,
            first
        )

        self.enter_text(
            CheckoutLocators.LAST_NAME,
            last
        )

        self.enter_text(
            CheckoutLocators.ADDRESS,
            address
        )

        self.enter_text(
            CheckoutLocators.POSTCODE,
            postcode
        )

        self.click(
            CheckoutLocators.CONTINUE
        )

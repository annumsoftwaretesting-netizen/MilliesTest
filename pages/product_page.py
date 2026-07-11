from pages.base_page import BasePage
from locators.product_locators import ProductLocators
from utilities.logger import get_logger


class ProductPage(BasePage):

    log = get_logger(__name__)

    def click_customise(self):

        self.click(
            ProductLocators.CUSTOMISE_BUTTON
        )

    def wait_for_product_page(self):

        self.wait_for_page_load()

    def select_cookie_type(self):

        self.log.info(
            "Current URL: %s",
            self.driver.current_url
        )

        swatches = self.driver.find_elements(
            *ProductLocators.COOKIE_SWATCH
        )

        self.log.info(
            "Swatches found: %d",
            len(swatches)
        )

        self.click(
            ProductLocators.COOKIE_SWATCH
        )

    def select_single_cookie(self):

        self.click(
            ProductLocators.SINGLE_COOKIE
        )

    def add_to_bag(self):

        self.click(
            ProductLocators.ADD_TO_BAG_BUTTON
        )

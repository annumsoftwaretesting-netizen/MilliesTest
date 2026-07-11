from pages.base_page import BasePage
from locators.product_locators import ProductLocators
 
 
class ProductPage(BasePage):
 
    def click_customise(self):
 
        self.click(
            ProductLocators.CUSTOMISE_BUTTON
        )
 
    def wait_for_product_page(self):
 
        self.wait_for_page_load()
 
    def select_cookie_type(self):
 
        print(
            "Current URL:",
            self.driver.current_url
        )
 
        swatches = self.driver.find_elements(
            *ProductLocators.COOKIE_SWATCH
        )
 
        print(
            f"Swatches found: {len(swatches)}"
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
           ADD_TO_BAG_BUTTON
        )
has context menu
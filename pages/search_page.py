from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from locators.search_locators import SearchLocators


class SearchPage(BasePage):

    def search_product(self, product):

        search_boxes = self.driver.find_elements(
            *SearchLocators.SEARCH_BOX
        )

        for box in search_boxes:

            if box.is_displayed():

                box.clear()

                box.send_keys(product)

                box.send_keys(Keys.ENTER)

                break

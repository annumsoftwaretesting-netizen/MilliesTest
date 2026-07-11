from utilities.environment import Environment

from locators.search_locators import SearchLocators

from components.cookie_banner_component import (
    CookieBannerComponent
)


def test_search_product(driver):

    driver.get(
        Environment.get_authenticated_url()
    )

    CookieBannerComponent(driver).accept_cookies()

    search_boxes = driver.find_elements(
        *SearchLocators.SEARCH_BOX
    )

    assert len(search_boxes) > 0

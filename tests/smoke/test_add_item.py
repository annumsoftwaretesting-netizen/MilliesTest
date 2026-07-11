from utilities.environment import Environment

from pages.product_page import ProductPage

from components.cookie_banner_component import (
    CookieBannerComponent
)


def test_add_item(driver):

    driver.get(
        Environment.get_authenticated_url()
        +
        "/giant-cookies/graduation"
    )

    CookieBannerComponent(driver).accept_cookies()

    product = ProductPage(driver)
    
    product.click_customise()

    product.wait_for_page_load()

    print(driver.current_url)

    product.select_cookie_type()

    product.select_single_cookie()

    product.add_to_bag()
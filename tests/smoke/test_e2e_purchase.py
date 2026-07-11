from utilities.environment import Environment

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.confirmation_page import ConfirmationPage

from components.cookie_banner_component import (
    CookieBannerComponent
)


def test_end_to_end_purchase(driver, test_user):

    driver.get(
        Environment.get_authenticated_url()
        +
        "/login"
    )

    CookieBannerComponent(driver).accept_cookies()

    LoginPage(driver).login(
        test_user["email"],
        test_user["password"]
    )

    driver.get(
        Environment.get_authenticated_url()
        +
        "/giant-cookies/graduation"
    )

    product = ProductPage(driver)

    product.click_customise()

    product.wait_for_page_load()

    product.select_cookie_type()

    product.select_single_cookie()

    product.add_to_bag()

    BasketPage(driver).checkout()

    CheckoutPage(driver).enter_details(
        "Annum",
        "Omar",
        "London Street",
        "E1 7AA"
    )

    PaymentPage(driver).pay(
        "4111111111111111",
        "12/30",
        "123"
    )

    order_number = (
        ConfirmationPage(driver)
        .get_order_number()
    )

    assert order_number != ""

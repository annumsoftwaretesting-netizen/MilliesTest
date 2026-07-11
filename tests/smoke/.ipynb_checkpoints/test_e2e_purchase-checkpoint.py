from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.confirmation_page import ConfirmationPage
 
 
def test_end_to_end_purchase(driver):
 
    driver.get(
        "https://www.milliescookies.com"
    )
 
    LoginPage(driver).login(
        "test@test.com",
        "Password123"
    )
 
    ProductPage(driver).add_to_basket()
 
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
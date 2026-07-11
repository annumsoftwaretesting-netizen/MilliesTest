from selenium.webdriver.common.by import By


class PaymentLocators:

    CARD_NUMBER = (
        By.ID,
        "cardNumber"
    )

    EXPIRY = (
        By.ID,
        "expiry"
    )

    CVV = (
        By.ID,
        "cvv"
    )

    PAY_BUTTON = (
        By.ID,
        "pay-now"
    )

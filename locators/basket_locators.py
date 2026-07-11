from selenium.webdriver.common.by import By


class BasketLocators:

    BASKET_COUNT = (
        By.CSS_SELECTOR,
        ".basket-count"
    )

    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        ".checkout-button"
    )

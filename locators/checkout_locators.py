from selenium.webdriver.common.by import By


class CheckoutLocators:

    FIRST_NAME = (
        By.ID,
        "firstName"
    )

    LAST_NAME = (
        By.ID,
        "lastName"
    )

    ADDRESS = (
        By.ID,
        "address"
    )

    POSTCODE = (
        By.ID,
        "postcode"
    )

    CONTINUE = (
        By.CSS_SELECTOR,
        ".continue-button"
    )

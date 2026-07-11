from selenium.webdriver.common.by import By


class LoginLocators:

    # the login inputs have no id attributes; the site exposes
    # cy-* test hooks on them instead
    EMAIL = (
        By.CSS_SELECTOR,
        "input[cy-loginmailinput]"
    )

    PASSWORD = (
        By.CSS_SELECTOR,
        "input[cy-loginpasswordinput]"
    )

    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        "button[type='submit']"
    )

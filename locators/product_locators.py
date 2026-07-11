from selenium.webdriver.common.by import By
 
 
class ProductLocators:
 
    CUSTOMISE_BUTTON = (
        By.XPATH,
        "//button[contains(.,'Customise')]"
    )
 
    COOKIE_SWATCH = (
        By.CSS_SELECTOR,
        "swatch"
    )
 
    SINGLE_COOKIE = (
        By.XPATH,
        "//span[contains(.,'Single')]"
    )
 
    ADD_TO_BAG_BUTTON = (
        By.CSS_SELECTOR,
        "button[cy-basketaddbutton]"
    )
 
    BASKET_ICON = (
        By.CSS_SELECTOR,
        ".basket"
    )
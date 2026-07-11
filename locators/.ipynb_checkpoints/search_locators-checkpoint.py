from selenium.webdriver.common.by import By
 
 
class SearchLocators:
 
    SEARCH_BOX = (
        By.CSS_SELECTOR,
        "input[name='search']"
    )
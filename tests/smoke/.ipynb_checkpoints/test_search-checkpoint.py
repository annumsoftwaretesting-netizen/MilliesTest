from selenium.webdriver.common.by import By
 
from utilities.environment import Environment
 
 
def test_search_product(driver):
 
    driver.get(
        Environment.get_authenticated_url()
    )
 
    search_boxes = driver.find_elements(
        By.CSS_SELECTOR,
        "input[name='search']"
    )
 
    print(
        "Search boxes:",
        len(search_boxes)
    )
 
    assert True
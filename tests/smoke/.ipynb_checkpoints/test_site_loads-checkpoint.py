from utilities.environment import Environment
 
 
def test_site_loads(driver):
 
    driver.get(
        Environment.get_authenticated_url()
    )
 
    assert "Millie's Cookies" in driver.title
from pages.login_page import LoginPage
 
 
def test_valid_login(driver):
 
    driver.get(
        "https://www.milliescookies.com/account/login"
    )
 
    login_page = LoginPage(driver)
 
    login_page.login(
        "test@test.com",
        "Password123"
    )
 
    assert "account" in driver.current_url.lower()
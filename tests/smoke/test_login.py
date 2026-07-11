from utilities.environment import Environment

from pages.login_page import LoginPage

from components.cookie_banner_component import (
    CookieBannerComponent
)


def test_valid_login(driver, test_user):

    driver.get(
        Environment.get_authenticated_url()
        +
        "/account/login"
    )

    CookieBannerComponent(driver).accept_cookies()

    login_page = LoginPage(driver)

    login_page.login(
        test_user["email"],
        test_user["password"]
    )

    assert "account" in driver.current_url.lower()

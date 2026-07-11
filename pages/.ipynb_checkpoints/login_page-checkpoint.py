from pages.base_page import BasePage
from locators.login_locators import LoginLocators
 
 
class LoginPage(BasePage):
 
    def login(self, email, password):
 
        self.enter_text(
            LoginLocators.EMAIL,
            email
        )
 
        self.enter_text(
            LoginLocators.PASSWORD,
            password
        )
 
        self.click(
            LoginLocators.LOGIN_BUTTON
        )
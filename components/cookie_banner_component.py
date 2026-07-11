from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class CookieBannerComponent:
 
    def __init__(self, driver):
        self.driver = driver
 
    def accept_cookies(self):
 
        try:
 
            print("Waiting for cookie banner...")
 
            accept_btn = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (
                        By.ID,
                        "onetrust-accept-btn-handler"
                    )
                )
            )
 
            print("Cookie banner found")
 
            self.driver.execute_script(
                "arguments[0].click();",
                accept_btn
            )
 
            print("Cookie banner clicked")
 
            WebDriverWait(
                self.driver,
                10
            ).until(
                EC.invisibility_of_element_located(
                    (
                        By.ID,
                        "onetrust-policy-text"
                    )
                )
            )
 
            print("Cookie banner disappeared")
 
        except Exception as e:
            print(
                f"Cookie banner error: {e}"
            )
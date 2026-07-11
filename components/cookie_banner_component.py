from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import get_logger


class CookieBannerComponent:

    ACCEPT_BUTTON = (
        By.ID,
        "onetrust-accept-btn-handler"
    )

    POLICY_TEXT = (
        By.ID,
        "onetrust-policy-text"
    )

    log = get_logger(__name__)

    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):

        try:

            self.log.info("Waiting for cookie banner...")

            accept_btn = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    self.ACCEPT_BUTTON
                )
            )

            self.log.info("Cookie banner found")

            self.driver.execute_script(
                "arguments[0].click();",
                accept_btn
            )

            self.log.info("Cookie banner clicked")

            WebDriverWait(
                self.driver,
                10
            ).until(
                EC.invisibility_of_element_located(
                    self.POLICY_TEXT
                )
            )

            self.log.info("Cookie banner disappeared")

        except TimeoutException:
            self.log.info(
                "Cookie banner not shown, continuing"
            )

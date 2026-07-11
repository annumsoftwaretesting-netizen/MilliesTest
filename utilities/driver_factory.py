from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import (
    Service as FirefoxService
)


class DriverFactory:

    @staticmethod
    def get_driver(browser, headless=False):

        browser = browser.lower()

        if browser == "chrome":

            options = webdriver.ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "edge":

            options = webdriver.EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = webdriver.FirefoxOptions()

            if headless:
                options.add_argument("-headless")

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

        else:
            raise ValueError(
                f"Browser {browser} not supported"
            )

        driver.maximize_window()

        return driver

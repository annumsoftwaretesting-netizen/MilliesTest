from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService
 
 
class DriverFactory:
 
    @staticmethod
    def get_driver(browser):
 
        browser = browser.lower()
 
        if browser == "chrome":
 
            driver = webdriver.Chrome(
                service=Service(
                    ChromeDriverManager().install()
                )
            )
 
        elif browser == "edge":
 
            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                )
            )
 
        else:
            raise Exception(
                f"Browser {browser} not supported"
            )
 
        driver.maximize_window()
 
        return driver
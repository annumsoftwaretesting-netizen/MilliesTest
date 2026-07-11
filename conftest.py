import pytest
 
from utilities.driver_factory import DriverFactory
 
 
def pytest_addoption(parser):
 
    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )
 
 
@pytest.fixture
def driver(request):
 
    browser = request.config.getoption(
        "--browser"
    )
 
    driver = DriverFactory.get_driver(
        browser
    )
 
    yield driver
 
    driver.quit()
 
 
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item,
    call
):
 
    outcome = yield
 
    report = outcome.get_result()
 
    if report.when == "call" and report.failed:
 
        driver = item.funcargs.get("driver")
 
        if driver:
 
            driver.save_screenshot(
                f"screenshots/{item.name}.png"
            )
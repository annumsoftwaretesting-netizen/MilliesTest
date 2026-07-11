import os

import pytest

from utilities.driver_factory import DriverFactory


def pytest_addoption(parser):

    parser.addoption(
        "--browser",
        action="store",
        default="chrome"
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False
    )


@pytest.fixture
def driver(request):

    browser = request.config.getoption(
        "--browser"
    )

    headless = request.config.getoption(
        "--headless"
    )

    driver = DriverFactory.get_driver(
        browser,
        headless=headless
    )

    yield driver

    driver.quit()


@pytest.fixture
def test_user():

    return {
        "email": os.environ.get(
            "TEST_USER_EMAIL",
            "test@test.com"
        ),
        "password": os.environ.get(
            "TEST_USER_PASSWORD",
            "Password123"
        ),
    }


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(
    item,
    call
):

    report = yield

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs(
                "screenshots",
                exist_ok=True
            )

            driver.save_screenshot(
                f"screenshots/{item.name}.png"
            )

    return report

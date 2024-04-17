import datetime
import pytest
import logging
import allure
import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    headless = request.config.getoption("--headless")
    executor_url = f"http://{executor}:4444/wd/hub"
    base_url = f"https://demo-opencart.ru/"  # https://demo-opencart.ru/

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"logs/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.datetime.now())
    )

    if browser_name == "chrome":
        option = ChromeOptions()
        if headless: option.add_argument('--headless')
    elif browser_name == "firefox":
        option = FirefoxOptions()
        if headless: option.add_argument('--headless')
    else:
        raise Exception("Driver not supported")
    
    # Set browser options
    option.add_argument("--start-maximized")
    option.add_argument("--disable-infobars")
    option.add_argument("--ignore-certificate-errors")

    # Set capability
    option.set_capability("browserVersion", os.getenv("VERSION"))
    selenoid_options = {
        "enableVideo": True,
        "enableVNC": True,
        "videoName": f"{os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]}.mp4",
        "name": os.environ.get("PYTEST_CURRENT_TEST").split(":")[-1].split(" ")[0]
    }
    option.set_capability("selenoid:options", selenoid_options)

    driver = webdriver.Remote(
        command_executor=executor_url, 
        options=option
    )

    driver.get(base_url)
    driver.maximize_window()

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    
    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities),
        attachment_type=allure.attachment_type.JSON,
    )

    logger.info("Browser %s started" % browser_name)

    def fin():
        driver.quit()
        logger.info(
            "===> Test %s finished at %s" % (
                request.node.name, datetime.datetime.now())
        )

    request.addfinalizer(fin)
    return driver

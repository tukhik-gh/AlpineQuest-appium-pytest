import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from config.config import PLATFORM_NAME, AUTOMATOR_NAME, DEVICE_NAME
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platformName = PLATFORM_NAME
    options.automationName = AUTOMATOR_NAME
    options.deviceName = DEVICE_NAME
    options.app = None
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield driver
    if driver:
        driver.quit()

def find_element_by_image_safe(driver, image_path):
    element = driver.find_element_by_image(image_path)
    if element is None:
        pytest.fail(f"element not found: {image_path}")
    return element

def find_element_by_image_with_timeout(driver, image_path, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(
            lambda d: d.find_element_by_image(image_path)
        )
    except NoSuchElementException:
        pytest.fail(f"Element not found using the provided image: {image_path}")

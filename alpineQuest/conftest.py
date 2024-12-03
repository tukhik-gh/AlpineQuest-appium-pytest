import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from utils.constants import PLATFORM_NAME, AUTOMATOR_NAME, DEVICE_NAME
import sys
import os

# Add the project root directory to the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture(scope="function")
def application():
    options = UiAutomator2Options()
    options.platformName = PLATFORM_NAME
    options.automationName = AUTOMATOR_NAME
    options.deviceName = DEVICE_NAME
    options.app = None
    application = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield application
    if application:
        application.quit()

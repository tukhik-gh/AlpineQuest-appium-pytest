import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep
import constants


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platformName = constants.PLATFORM_NAME
    options.automationName = constants.AUTOMATION_NAME
    options.deviceName = constants.DEVICE_NAME
    options.app = None
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    yield driver
    if driver:
        driver.quit()


def test_open_alpine_quest(driver):
    try:
        app_icon = driver.find_element(
            AppiumBy.XPATH,
            "//*[@content-desc='AlpineQuest']"
        )
    except:
        app_icon = driver.find_element(
            AppiumBy.XPATH,
            "//*[@text='AlpineQuest']"
        )

    app_icon.click()
    assert "The 'Alpine quest' app has been launched."
    sleep(5)

def test_app_launch(driver):
    test_open_alpine_quest(driver)
    assert driver.current_activity == ".NexusLauncherActivity" or driver.current_activity == ".AlpineQuestActivity", "App failed to launch."
    sleep(5)

def test_create_waypoint(driver):
    test_open_alpine_quest(driver)
    parent_element = driver.find_elements(AppiumBy.XPATH, '[@resource-id="android:id/content"]')
    child_elements = parent_element.find_elements(AppiumBy.XPATH, "./*")

    print(child_elements, "All element ======")

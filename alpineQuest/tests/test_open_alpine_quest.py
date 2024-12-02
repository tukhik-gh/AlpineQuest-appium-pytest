from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
from conftest import driver

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

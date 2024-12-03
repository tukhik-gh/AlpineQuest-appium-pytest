from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

def test_open_alpine_quest(application):
    try:
        app_icon = application.find_element(
            AppiumBy.XPATH,
            "//*[@content-desc='AlpineQuest']"
        )
    except:
        app_icon = application.find_element(
            AppiumBy.XPATH,
            "//*[@text='AlpineQuest']"
        )
    app_icon.click()
    assert "The 'Alpine quest' app has been launched."
    sleep(2)

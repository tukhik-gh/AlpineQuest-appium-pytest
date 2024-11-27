from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from tests.conftest import find_element_by_image_with_timeout
from tests.test_open_alpine_quest import test_open_alpine_quest
# from appium.webdriver.common.touch_action import TouchAction

def test_create_waypoint(driver):
    test_open_alpine_quest(driver)
    sleep(12)

    # Step 1
    try:
        element = WebDriverWait(driver, 10).until(
            find_element_by_image_with_timeout(driver, "../images/menu.png")
        )
        element.click()
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        driver.quit()
        print("Driver status:", driver.capabilities)
        print("Trying to find element by image...")
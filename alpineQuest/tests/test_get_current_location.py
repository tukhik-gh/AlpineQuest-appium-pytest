from time import sleep
from utils.helpers import find_and_click_button, find_element_by_xpath
from tests.test_open_alpine_quest import test_open_alpine_quest

def test_get_current_location(driver):
    # Step 1: Open the app.
    test_open_alpine_quest(driver)
    # The app is successfully launched.
    sleep(1)

    # Step 2: Click GPS icon
    find_and_click_button(driver, '../images/position.jpg')
    sleep(1)
    find_element_by_xpath(driver, '//*[@text="POSITIONING"]')

    # Step 3: Switch on GPS
    position_element = find_element_by_xpath(driver, '(//android.widget.Switch[@text="OFF"])[1]')
    position_element.click()
    assert position_element.text != "OFF", "First switch did not change state or was not clicked."
    switch_on = find_element_by_xpath(driver, '//android.widget.Switch[@text="ON"]')
    assert switch_on != "", "Real-time position is on"
    sleep(1)

    # Step 4: Click GPS button and close modal
    find_and_click_button(driver, '../images/position_on_red.png')

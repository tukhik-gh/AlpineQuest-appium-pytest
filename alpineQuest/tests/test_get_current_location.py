from time import sleep
from utils.helpers import find_and_click_button, find_element_by_xpath
from tests.test_open_alpine_quest import test_open_alpine_quest
from pages.positioning import PositioningPage

def test_get_current_location(application):
    # Step 1: Open the app.
    positioning_page = PositioningPage(application)
    positioning_page.open()
    # The app is successfully launched.
    sleep(1)

    # Step 2: Click GPS icon
    positioning_page.menuButton()
    sleep(1)
    positioning_page.finedModalTitle()

    # Step 3: Switch on GPS
    gps_switch = positioning_page.finedLocationSwitch()
    gps_switch.click()
    assert gps_switch.text != "OFF", "First switch did not change state or was not clicked."
    switch_on = positioning_page.finedLocationGPSOnSwitch()
    assert switch_on != "", "Real-time position is on"
    sleep(1)

    # Step 4: Click GPS button and close modal
    positioning_page.closeGPSModal()

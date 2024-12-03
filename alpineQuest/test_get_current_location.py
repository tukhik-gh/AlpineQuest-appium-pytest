from time import sleep
from alpineQuest.pages.positioning_page import PositioningPage

def test_get_current_location(application):
    # Step 1: Open the app.
    positioning_page = PositioningPage(application)
    positioning_page.open_app()
    # The app is successfully launched.
    sleep(1)

    # Step 2: Click GPS icon
    positioning_page.click_menu_button()
    sleep(1)
    positioning_page.fined_modal_title()

    # Step 3: Switch on GPS
    gps_switch = positioning_page.fined_switch_location_button()
    gps_switch.click()
    assert gps_switch.text != "OFF", "First switch did not change state or was not clicked."
    switch_on = positioning_page.fined_and_click_location_gps_on_button()
    assert switch_on != "", "Real-time position is on"
    sleep(1)

    # Step 4: Click GPS button and close modal
    positioning_page.close_gps_modal()

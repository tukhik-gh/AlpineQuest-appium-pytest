from time import sleep
from alpineQuest.pages.gps_page import PositioningPage
from utils.constants import GPS_PAGE_TITLE, OFF

def test_get_current_location(application):
    # Step 1: Open the app.
    gps_page = PositioningPage(application)
    gps_page.open_app()
    # The app is successfully launched.
    sleep(1)

    # Step 2: Click GPS icon
    gps_page.click_gps_button()
    sleep(1)
    modal_title = gps_page.fined_modal_title()
    assert modal_title.text == GPS_PAGE_TITLE, f'The title of the modal is not {GPS_PAGE_TITLE}'

    # Step 3: Switch on GPS
    gps_switch = gps_page.fined_switch_location_button()
    gps_switch.click()
    assert gps_switch.text != OFF, "First switch did not change state or was not clicked."
    switch_on = gps_page.fined_and_click_location_gps_on_button()
    assert switch_on != "", "Real-time position is on"
    sleep(1)

    # Step 4: Click GPS button and close modal
    gps_page.close_gps_modal()

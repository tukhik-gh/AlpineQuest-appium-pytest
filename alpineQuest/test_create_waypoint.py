from time import sleep
from alpineQuest.pages.placemarks_page import PlaceMarks
from utils.constants import PLACE_MARKS, LOCAL_PLACE_MARKS, WAYPOINT

def test_create_waypoint(application):
    # Step 1: Open the app.
    place_mark_page = PlaceMarks(application)
    place_mark_page.open_app()
    # The app is successfully launched.
    sleep(1)

    # Step 2: Click pleacemark icon
    place_mark_page.click_place_marks_button()
    sleep(1)
    modal_title = place_mark_page.fined_modal_title()
    assert modal_title.text == PLACE_MARKS, f'The title of the modal is not {PLACE_MARKS}'

    # Step 3: Click create a placemark button
    place_mark_page.fined_create_a_place_mark_button()
    sleep(1)
    local_placemarks_modal_title = place_mark_page.fined_local_placemarks_modal_title()
    assert local_placemarks_modal_title.text == LOCAL_PLACE_MARKS, f'The title of the modal is not {LOCAL_PLACE_MARKS}'

    # Step 4:  Find and click waypoint button
    waypoint_button = place_mark_page.find_waypoint_button()
    waypoint_button.onclick()
    sleep(1)
    waypoint_modal_title = place_mark_page.fined_waypoint_modal_title()

    assert waypoint_modal_title.is_displayed()
    assert waypoint_modal_title.text == WAYPOINT, f'The title of the modal is not {WAYPOINT}'

    # Step 5:  Create waypoint
    input_field = place_mark_page.fined_name_input_selector
    input_field.clear()
    input_field.send_keys("Test Waypoint")
    assert input_field.text == "Test Waypoint", "Text input failed."

from time import sleep
from utils.helpers import find_and_click_button
from tests.test_open_alpine_quest import test_open_alpine_quest
import time


def test_create_waypoint(application):
    test_open_alpine_quest(application)
    sleep(12)
    click_x, click_y = find_and_click_button(application, 'button_image.png')
    if click_x is not None and click_y is not None:
        application.tap([(click_x, click_y)])  # Perform the click action
    else:
        print("Button not found or failed to load images.")


def main(application):
    time.sleep(5)  # Adjust sleep time as needed for the app to load
    button_image_path = 'path_to_your_button_image.png'  # Replace with your button image path

    if find_and_click_button(application, button_image_path):
        # Define locator for the expected outcome (example: ID of an element that should be displayed)
        expected_element_locator = ('id', 'expected_element_id')  # Adjust as necessary


    application.quit()

if __name__ == '__main__':
    main()
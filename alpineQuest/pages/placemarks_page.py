from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy
from alpineQuest.utils.constants import PLACE_MARKS, LOCAL_PLACE_MARKS, WAYPOINT

place_mark_text_selector = (AppiumBy.XPATH, f'//*[@text="Create a {PLACE_MARKS}"]')
modal_title_selector = (AppiumBy.XPATH, f'//*[@text={PLACE_MARKS}]')
locale_placemarks_modal_title_selector = (AppiumBy.XPATH, f'//*[@text={LOCAL_PLACE_MARKS}]')
place_mark_button_selector = './images/place_marks.png'
waypoint_selector = (AppiumBy.XPATH, f'//*[@text={WAYPOINT}]')
waypoint_modal_selector = (AppiumBy.XPATH,  f'//*[@text={WAYPOINT}]')
name_input_selector = (AppiumBy.XPATH,  '//*[@text="Optional"]')


class PlaceMarks(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()

    def click_place_marks_button(self):
        return self.find_and_click_button_by_image(place_mark_button_selector)

    def fined_modal_title(self):
        return self.find(modal_title_selector)

    def fined_local_placemarks_modal_title(self):
        return self.find(locale_placemarks_modal_title_selector)

    def fined_create_a_place_mark_button(self):
        return self.find(place_mark_text_selector)

    def fined_waypoint_button(self):
        return self.find(place_mark_text_selector)

    def find_waypoint_button(self):
        return self.find(waypoint_selector)

    def fined_waypoint_modal_title(self):
        return self.find(waypoint_modal_selector)

    def fined_name_input_selector(self):
        return self.find(name_input_selector)

    def close_gps_modal(self):
        return self.find_and_click_button_by_image(place_mark_button_selector)


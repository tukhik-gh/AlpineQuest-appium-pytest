from alpineQuest.pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


switch_off_selector = (AppiumBy.XPATH, '(//android.widget.Switch[@text="OFF"])[1]')
switch_on_selector = (AppiumBy.XPATH, '//android.widget.Switch[@text="ON"]')
modal_title = (AppiumBy.XPATH, '//*[@text="POSITIONING"]')
menu_button_selector = './images/position.png'
close_gps_modal = './images/position_on_red.png'


class PositioningPage(BasePage):

    def __init__(self, application):
        super().__init__(application)

    def open_app(self):
        return self.open_application()
    
    def click_gps_button(self):
        return self.find_and_click_button_by_image(menu_button_selector)

    def fined_modal_title(self):
        return self.find(modal_title)
    
    def fined_switch_location_button(self):
        return self.find(switch_off_selector)

    
    def fined_and_click_location_gps_on_button(self):
        return self.find(switch_on_selector)
    
    def close_gps_modal(self):
        return self.find_and_click_button_by_image(close_gps_modal)

    
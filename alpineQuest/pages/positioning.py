from base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

switch_off_selector = (AppiumBy.XPATH, '(//android.widget.Switch[@text="OFF"])[1]')
switch_on_selector = (AppiumBy.XPATH, '//android.widget.Switch[@text="ON"]')
modal_title = (AppiumBy.XPATH, '//*[@text="POSITIONING"]')
menu_button_selector = ('../images/position.jpg')
close_gps_modal = (AppiumBy.XPATH,'../images/position_on_red.png')

class PositioningPage(BasePage):
    def __init__(self, application):
        super().__init__(application)
    
    def menuButton(self):
        return self.findAndClickButton(self.application, menu_button_selector)
    
    def finedLocationSwitch(self):
        return self.find(switch_off_selector)
    
    def finedModalTitle(self):
        return self.find(modal_title)
    
    def finedLocationGPSOnSwitch(self):
        return self.find(switch_on_selector)
    
    def closeGPSModal(self):
        return self.findAndClickButton(self.application, menu_button_selector)

    
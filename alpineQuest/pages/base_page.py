import cv2
import numpy as np
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    def __init__(self, application):
        self.application = application

    def open_application(self):
        try:
            app_icon = self.application.find_element(
            AppiumBy.XPATH,
            "//*[@content-desc='AlpineQuest']"
        )
        except:
            app_icon = self.application.find_element(
            AppiumBy.XPATH,
            "//*[@text='AlpineQuest']"
        )
        app_icon.click()
        assert "AlpineQuest" in self.application.current_activity, "The 'Alpine Quest' app has not been launched."
        sleep(2)

    def find(self, args):
        return self.application.find_element(*args)

    def capture_screenshot(self):
        screenshot = self.application.get_screenshot_as_png()
        with open('./screenshots/screen.png', 'wb') as file:
            file.write(screenshot)
        
        
    def find_and_click_button(self, button_image_path):
        self.capture_screenshot()

        # Load the screenshot
        screenshot = cv2.imread('./screenshots/screen.png')

        # Load the button image
        button_image = cv2.imread(button_image_path)

        # Use OpenCV to find the button in the screenshot
        result = cv2.matchTemplate(screenshot, button_image, cv2.TM_CCOEFF_NORMED)
        threshold = 0.8  # Adjust depending on how strict the match should be
        yloc, xloc = np.where(result >= threshold)

        # If a match is found, click on it
        if len(xloc) > 0:
            # Get the location of the first match
            x = xloc[0]
            y = yloc[0]

            # Calculate the center of the matched region
            button_height, button_width = button_image.shape[:2]
            click_x = x + button_width / 2
            click_y = y + button_height / 2

            # Perform the click action
            self.application.tap([(click_x, click_y)])
            print(f'Clicked on button at ({click_x}, {click_y})')
        else:
            print('Button not found')

    
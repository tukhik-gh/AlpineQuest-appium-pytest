import cv2
import numpy as np

from appium.webdriver.common.appiumby import AppiumBy

# Function to capture screenshot and save it
def capture_screenshot(driver):
    screenshot = driver.get_screenshot_as_png()
    with open('../screenshots/screen.png', 'wb') as file:
        file.write(screenshot)

# Function to find and click on the button image
def find_and_click_button(driver, button_image_path):
    capture_screenshot(driver)

    # Load the screenshot
    screenshot = cv2.imread('../screenshots/screen.png')

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
        driver.tap([(click_x, click_y)])
        print(f'Clicked on button at ({click_x}, {click_y})')
    else:
        print('Button not found')


def find_element_by_xpath(driver, xpath):
    try:
        element = driver.find_element(by=AppiumBy.XPATH, value=xpath)

        assert element is not None, "Element not found"

        return element
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

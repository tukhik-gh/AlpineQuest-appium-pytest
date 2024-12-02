# Initialize Appium driver
# def initialize_driver():
#     desired_caps = {
#         'platformName': 'Android',
#         'deviceName': 'YourDeviceName',  # Replace with your device name
#         'app': 'YourAppPackageName',  # Replace with your app package name
#         'noReset': True,
#         'automationName': 'UiAutomator2',
#     }
#     driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#     return driver
#





# def main(driver):
#     time.sleep(5)  # Adjust sleep time as needed for the app to load
#     button_image_path = '../images/maps.png'  # Replace with your button image path
#     test_find_and_click_button(driver, button_image_path)
#     driver.quit()
#
#
# if __name__ == '__main__':
#     main()
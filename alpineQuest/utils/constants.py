APPIUM_SERVER_URL = "http://localhost:4723/wd/hub"

DEVICE_NAME = "Android Emulator"
PLATFORM_NAME = "Android"
PLATFORM_VERSION = "13"
AUTOMATOR_NAME = "uiautomator2"
APP_NAME = "AlpineQuest"

DESIRED_CAPS = {
    'platformName': PLATFORM_NAME,
    'platformVersion': PLATFORM_VERSION,
    'deviceName': DEVICE_NAME,
    'automationName': AUTOMATOR_NAME,
    'noReset': True,
    'fullContextList': True,
    'newCommandTimeout': 600,
}

TIMEOUT = 30



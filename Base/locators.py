from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from appium.webdriver.appium_service import AppiumService # import appium service class

appium_service = AppiumService() # create object for appium service class

appium_service.start() # call start method by using appium service class object

# Create "Desired Capabilities"
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.platform_version = '14'  # Update this to the correct Android version
options.device_name = '79003d15'
options.app = 'D:\\PyProjects\\Android_Demo_App.apk'
options.app_package = "com.code2lead.kwad"
#options.no_reset = True
options.full_reset = True
options.new_command_timeout = 300  # Adding a timeout

# Launch App
try:
    driver = webdriver.Remote('127.0.0.1:4723', options=options)

# Click on the App
    ele_id = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)" )
    ele_id.click()

# Wait for 2 seconds
    time.sleep(2)

finally:
# Close the driver object
    driver.quit()

appium_service.stop() # call stop method by using appium service class object
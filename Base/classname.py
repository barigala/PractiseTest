from appium import webdriver
import time
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Create "Desired Capabilities"
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.platform_version = '14'  # Update this to the correct Android version
options.device_name = '79003d15'
options.app = 'D:\\PyProjects\\Android_Demo_App.apk'
options.app_package = "com.code2lead.kwad"
#options.no_reset = True
#options.full_reset = True
options.new_command_timeout = 300  # Adding a timeout

# Launch App
try:
    driver = webdriver.Remote('127.0.0.1:4723', options=options)

# Click on the App
    ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
    ele_id.click()
    time.sleep(2)
    ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
    ele_classname.send_keys("SunilB")

# Wait for 2 seconds
    time.sleep(2)

finally:
# Close the driver object
    driver.quit()
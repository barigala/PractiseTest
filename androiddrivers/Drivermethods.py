from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.platform_version = '14'  # Update this to the correct Android version
options.device_name = '79003d15'
options.app = 'D:\\PyProjects\\Android_Demo_App.apk'
options.app_package = "com.code2lead.kwad"

driver = webdriver.Remote('127.0.0.1:4723', options=options)

print("Check if device is locked or not:",driver.is_locked())
print("Current Package:", driver.current_package)
print("Current Activity:", driver.current_activity)
print("Current Context:", driver.current_context)
print("Current Orientation:", driver.orientation)
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

from Base.methods import elements

options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.platform_version = '14'  # Update this to the correct Android version
options.device_name = '79003d15'
options.app = 'D:\\PyProjects\\Android_Demo_App.apk'
options.app_package = "com.code2lead.kwad"

driver = webdriver.Remote('127.0.0.1:4723', options=options)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")

print("Is Displayed:", ele_id.is_displayed())
print("Is Enabled:", ele_id.is_enabled())
print("Is Selected:", ele_id.is_selected())
print("Size:", ele_id.size)
print("location:",ele_id.location)

driver.quit()
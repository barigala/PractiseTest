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

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()
time.sleep(2)
ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
ele_classname.send_keys("SunilB")
ele_classname.click()


driver.press_keycode(67)
driver.press_keycode(67)

time.sleep(2)

driver.press_keycode(4)
driver.press_keycode(4)

time.sleep(2)

driver.quit()
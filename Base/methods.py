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

elements = driver.find_elements(AppiumBy.CLASS_NAME,"android.widget.Button")

for abc in elements:
    print(abc.text)

for efg in elements:
    buttton = efg.text
    if buttton == "ScrollView":
        efg.click()
        break

time.sleep(2)
driver.quit()

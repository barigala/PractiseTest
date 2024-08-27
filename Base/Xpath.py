import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from Base.locators import ele_id

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
    ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="ENTER SOME VALUE"]')
    ele_xpath.click()

    time.sleep(2)

finally:
# Close the driver object
    driver.quit()
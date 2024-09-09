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

ele_xpath = driver.find_element(AppiumBy.XPATH,
                                '//android.widget.Button[@content-desc="Btn1"]')  # By using xpath and Con-des
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.code2lead.kwad:id/EnterValue"]') Xpath and Res-id
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@text="ENTER SOME VALUE"]') Xpath and text
# ele_xpath = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[3]') xpath and Index value
ele_xpath.click()

time.sleep(2)

ele_xpath2 = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
ele_xpath2.send_keys("Skill2lead.com")

time.sleep(2)

driver.quit()

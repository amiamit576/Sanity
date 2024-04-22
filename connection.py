import time
import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC




capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='fc20c0534',
    language='en',
    locale='US',
    ignoreHiddenApiPolicyError='true',
    noReset='true'
)




'''recciver_capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    udid='192.168.1.63:5555',
    language='en',
    locale='US',
    ignoreHiddenApiPolicyError='true',
    noReset='true'
)'''
Host_Url='http://localhost:4723'

driver=webdriver.Remote(Host_Url, options=UiAutomator2Options().load_capabilities(capabilities))
#recciverdriver=webdriver.Remote(Host_Url, options=UiAutomator2Options().load_capabilities(recciver_capabilities))
count=0

driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Phone').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'key pad').click()
time.sleep(1)
#number=input("Enter the number-->")
number='9871052407'
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.google.android.dialer:id/digits"]').send_keys(number)
driver.find_element(AppiumBy.ACCESSIBILITY_ID,'dial').click()
time.sleep(10)
# reciever devices
#cordinates=(948,504)
#recciverdriver.tap([cordinates])
wait_to_recciveTheCall=WebDriverWait(driver,30)
try:
    wait_to_recciveTheCall.until(
     EC.visibility_of_element_located((AppiumBy.XPATH,'//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'))
    )
    time.sleep(26)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="End call"]').click()
except:
    print("Call Bloc")
    count += 1
print("hello")
# wait for 5sec


for i in range(5):
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.google.android.dialer:id/primary_text" and @text="Ayn"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="call Ayn"]').click()
    wait_to_recciveTheCall = WebDriverWait(driver, 35,poll_frequency=1)
    try:
        wait_to_recciveTheCall.until(
            EC.visibility_of_element_located((AppiumBy.XPATH,
                                              '//android.widget.Chronometer[@resource-id="com.google.android.dialer:id/contactgrid_bottom_timer"]'))
        )
        time.sleep(26)
        call_end = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="End call"]').click()
    except:
        print("Call Bloc")
        count += 1
print('The Call BlocCount is :',count)



























import time
import pytest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
capabilities = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'fc20c0534',
    'language': 'en',
    'locale': 'US',
    'ignoreHiddenApiPolicyError': True,
    'noReset': True
}

Host_Url = 'http://localhost:4723'
driver = webdriver.Remote(Host_Url, options=UiAutomator2Options().load_capabilities(capabilities))

package_name = 'com.google.android.apps.messaging'  # Replace with the package name of your app
activity_name = 'com.google.android.apps.messaging.ui.ConversationListActivity'  # Replace with the activity name of your app

driver.swipe(523,2308,523,686)
time.sleep(1)
driver.swipe(523,2308,523,686)
driver.find_element(AppiumBy.XPATH,'(//android.widget.TextView[@content-desc="Messages"])[2]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@content-desc="Start chat"]').click()
number=input("Enter the num  you want to send  Sms: ")
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="ContactSearchField"]').send_keys(number)
driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Send to ~Amit Kumar"]').click()
paragraph=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed tristique mi id risus aliquam, nec hendrerit eros molestie. Integer ut nisi eget nunc vulputate condimentum. Nulla ac leo ac ipsum condimentum rhoncus. Vivamus nec est a ligula tincidunt rutrum sit amet nec ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce non dolor vel nunc lacinia accumsan. Sed ultricies ipsum id ipsum ultricies, nec dapibus tortor tempus. Nullam euismod metus sit amet velit lacinia, id eleifend velit viverra. Quisque in diam vitae nisi varius sollicitudin. "
           "Cras eget metus nec sapien rutrum hendrerit. Mauris vulputate luctus sapien, ut sollicitudin orci volutpat non. Ut non feugiat justo, a elementum nibh. Curabitur vel justo ut nulla vehicula interdum.")
driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.google.android.apps.messaging:id/compose_message_text"]').send_keys(paragraph)
time.sleep(1)
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageView[@content-desc="Send SMS"]').click()
no_count=int(input("Number of time you want input a number : "))
for i in range(no_count):
    driver.find_element(AppiumBy.XPATH,
                        '//android.widget.EditText[@resource-id="com.google.android.apps.messaging:id/compose_message_text"]').send_keys(
        paragraph)
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Send SMS"]').click()
driver.find_element(AppiumBy.XPATH,'//android.widget.ImageButton[@content-desc="Navigate up"]').click()
driver.execute_script('mobile: pressKey', {"keycode": 4})









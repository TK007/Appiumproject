import time

import touch as touch
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "platformName": "Android",
    "deviceName": "ca5ac45e",
    "platformVersion": "10",
    "appPackage": "com.flipkart.android",
    "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
    "newCommandTimeout": "60"
}
driver = webdriver.Remote("http://localhost:4724/wd/hub", desired_cap)
driver.implicitly_wait(30)

# Get the price of Bed and verify it
driver.find_element_by_class_name("android.widget.ImageButton").click()
# AllCat = driver.find_element_by_id("flyout_parent_title")
# driver.set_value(AllCat, 'All Categories')


driver.find_element_by_xpath("//*[@text='All Categories']").click()
driver.find_element_by_xpath("//*[@bounds='[360,1002][720,1386]']").click()
driver.find_element_by_xpath("//*[@bounds='[0,930][270,1294]']").click()

""""
Touch Actions
"""
# touch = TouchAction(driver)
# touch.press(x=543, y=1010).move_to(x=543, y=366).release().perform()
# time.sleep(3)

for i in range(6):
    touch = TouchAction(driver)
    touch.press(x=273, y=500).move_to(x=273, y=166).release().perform()
    time.sleep(5)



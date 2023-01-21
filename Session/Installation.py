import time

import driver as driver
#from appium.webdriver.common.keys import Keys

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#from appium.webdriver.common.multi_action import MultiAction
#from selenium.webdriver.common.action_chains import ActionChains
#import time
#import os
#import math
#import random
#import smtplib
from twilio.rest import Client
#import random
#import tkinter import *
#import tkinter import messagebox

desired_cap = {
    "platformName" : "Android",
    "PlatformVersion" : "10",
    "deviceName" : "ca5ac45e",
    "appPackage" : "com.prepladder.medicalprep",
    "appActivity" : "com.prepladder.medical.prepladder.SplashActivity",
    "newcommandTimeout" : "60",
    "autoGrantPermissions" : "true",
    "autoAcceptAlerts" : "true",
    "autoDissmissAlerts" : "true"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(40)
print("Run")
driver.set_script_timeout(4000)
# Step 5 : Find the device width and height
# deviceSize = driver.get_window_size()
# print("Device Width and Height : ",deviceSize)
# screenWidth = deviceSize['width']
# screenHeight = deviceSize['height']
#
# # Step 6 : Find the x,y coordinate to swipe
# # *********** Swiping from Bottom to Top ************* #
# startx = screenWidth*0.90
# endx = screenWidth*0.05
# starty = screenHeight/2
# endy = screenHeight/9
#
#
# time.sleep(5)
# actions = TouchAction(driver)
# actions.press(None,startx,starty).move_to(None,endx,starty).release().perform()
# time.sleep(2)
# #
# for i in range(3):
actions = TouchAction(driver)
#      actions.press(None, startx, starty).move_to(None, endx, starty).release().perform()
#      time.sleep(2)
#
# driver.find_element_by_id("lets").click()

driver.find_element_by_id("arrow_imv").click()
search = driver.find_element_by_id("search_edt")
search.send_keys("United States")
driver.find_element_by_id("country_name_tv").click()


phone = driver.find_element_by_xpath("//*[@class='android.widget.EditText']")
# # #actions.tap(x=361, y=854).perform()
phone.send_keys("3252307093")
actions.long_press(phone).perform()

# driver.find_element_by_xpath("//*[@text='Or continue with email']").click()
driver.find_element_by_id("click_continue").click()
time.sleep(20)


# Twilio = driver.find_element_by_id("")
# client = Client("ssid=AC61db60418982c93b5d564640c67fe880","auth token=b9bcbb5a7ea3f966f625874841289773")
# client.messages.create(
#     to=["+919988163919"],
#     from_="+13252307093",
#     body="This was sent from twilio")

account_sid = "AC61db60418982c93b5d564640c67fe880"
auth_token = "b9bcbb5a7ea3f966f625874841289773"
client = Client(account_sid, auth_token)
messages = client.messages.list(limit=1)

for record in messages:

    otp = record.body[4:10]

print(otp)
list(otp)
a,b,c,d,e,f = list(otp)

user = driver.find_element_by_id("otp_editText1")
user.send_keys(a)
user= driver.find_element_by_id("otp_editText2")
user.send_keys(b)
user= driver.find_element_by_id("otp_editText3")
user.send_keys(c)
user = driver.find_element_by_id("otp_editText4")
user.send_keys(d)
user = driver.find_element_by_id("otp_editText5")
user.send_keys(e)
user = driver.find_element_by_id("otp_editText6")
user.send_keys(f)
driver.find_element_by_id("verify").click()

enterName = driver.find_element_by_id("name")
enterName.send_keys("Tarun Kaushik")
actions.long_press(enterName).perform()

emailID = driver.find_element_by_id("email")
emailID.send_keys("Python@gmail.com")
actions.long_press(emailID).perform()

driver.find_element_by_xpath("//*[@text='']").click()

#driver.find_element_by_xpath("").send_keys(Keys.HOME)
#el = driver.find_element_by_xpath("//*[@text='Nepal']") driver.execute_script("mobile: scrollTo", {"element": el.id})




# element_to_tap = driver.find_element_by_xpath("//*[@text='India']")
# driver.find_element_by_xpath(<xpath_to_element_near_bottom_of_screen>)
# element_to_drag_to =
# driver.find_element_by_xpath(<xpath_to_element_near_top_of_screen>)
# driver.scroll(element_to_tap, element_to_drag_to)


# el = self.driver.find_element_by_xpath(“//*[@text='Nepal']”)
# self.driver.execute_script(“mobile: scroll”, {“direction”: ‘down’, ‘element’: el,})
#

for i in range(5):
    touch = TouchAction(driver)
    touch.press(x=138, y=1900).move_to(x=138, y=1561).release().perform()
    time.sleep(5)













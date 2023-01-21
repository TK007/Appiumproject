"""
Video recording steps
1.) Create file path using (os.path.join (directory,filename)
2.) Save the video base64 file from stop recording method
3.) Convert base64 into media file (mp4) using with <expression> as <variable>: decode base64 file
"""
import base64
import os
import time

# import touch as touch
from appium import webdriver

# from appium.webdriver.common.touch_action import TouchAction

desired_cap = {
    "platformName": "Android",
    "deviceName": " ca5ac45e",
    "platformVersion": "10",
    "appPackage": "com.flipkart.android",
    "appActivity": "com.flipkart.android.activity.HomeFragmentHolderActivity",
    "newCommandTimeout": "60"
}
driver = webdriver.Remote("http://localhost:4724/wd/hub", desired_cap)
driver.implicitly_wait(30)
# start video recording

driver.start_recording_screen()

driver.find_element_by_class_name("android.widget.ImageButton").click()
driver.find_element_by_xpath("//*[@text='All Categories']").click()
driver.find_element_by_xpath("//*[@bounds='[360,1002][720,1386]']").click()
driver.find_element_by_xpath("//*[@bounds='[0,930][270,1294]']").click()

video_rawdata = driver.stop_recording_screen()

video_name = driver.current_activity + time.strftime("%Y_%M_%D_%H%M%S")

#filepath = os.path.join("C:\Users\user\PycharmProjects\Appiumproject\Session", video_name + ".mp4")

with open(filepath, "wb") as vd:
    vd.write(base64.b64decode(video_rawdata))

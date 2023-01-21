from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "ca5ac45e",
    "platformVersion": "10",
    "appPackage": "com.cricbuzz.android",
    "appActivity": "com.cricbuzz.android.lithium.app.view.activity.NyitoActivity"
}

driver = webdriver.Remote("http://localhost:4724/wd/hub", desired_cap)
print("RUN")

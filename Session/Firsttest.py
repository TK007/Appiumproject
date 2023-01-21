from appium import webdriver


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

# Get the price of item and verify it
driver.find_element_by_class_name("android.widget.ImageButton").click()
# AllCat = driver.find_element_by_id("flyout_parent_title")
# driver.set_value(AllCat, 'All Categories')


driver.find_element_by_xpath("//*[@text='All Categories']").click()
driver.find_element_by_xpath("//*[@bounds='[360,1002][720,1386]']").click()
driver.find_element_by_xpath("//*[@bounds='[0,1788][270,2148]']").click()
price = driver.find_element_by_xpath("//*[@bounds='[159,1030][297,1076]']").get_attribute("text")
print(" New Price is " +price)

assert price == "18999", "The price is not matched"


#menu = driver.find_elements_by_id("flyout_parent_title")
# for items in menu:
#     print(items.text)
#     if items.text == "All Categories":
#         items.click()





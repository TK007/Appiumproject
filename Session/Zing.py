from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"
chrome_options = Options()
#chrome_options.add_argument("--disable-web-security")
#chrome_options.add_argument("test-type")
chrome_options.add_argument("--start-maximized")
capabilities = chrome_options.to_capabilities()
driver = webdriver.Chrome(chrome, desired_capabilities=capabilities)
driver.get("https://portal.zinghr.com/2015/pages/authentication/login.aspx")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/input").send_keys("prepladder")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/input").send_keys("EMP320")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[4]/input").send_keys("Napolean@2")
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div/div[1]/div[2]/div[7]/button")
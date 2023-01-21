import time
from concurrent.futures import thread

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

desired_cap = {
    "platformName": "chrome"
}
chrome = "C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe"
email = "Tarun.kaushik@prepladder.com"
password = "prepladder123"

# def login():
chrome_options = Options()

chrome_options.add_argument("--disable-web-security")

chrome_options.add_argument("test-type")
chrome_options.add_argument("--start-maximized")
capabilities = chrome_options.to_capabilities()
driver = webdriver.Chrome(chrome, desired_capabilities=capabilities)
driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("Tarunkaushik.prepladder@gmail.com")
driver.find_element_by_xpath("//span[text()='Next']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@type='password']").send_keys("prepladder123")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()


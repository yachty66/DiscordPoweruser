from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import config

TOKEN = config.token
EMAIL = "wobbert2503@gmail.com"
PASSWORD = config.password

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)
url = 'https://discord.com/login'
driver.get(url)

time.sleep(15)
driver.get("https://discord.com/channels/1048287921138040843")
time.sleep(7)

member_list_button = driver.find_element("xpath", "//div[@aria-label='Show Member List']")

member_list_button.click()

# Wait for Discord to log in and load
time.sleep(15)
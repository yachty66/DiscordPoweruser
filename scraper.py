from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import config

TOKEN = config.token
EMAIL = "wobbert2503@gmail.com"
PASSWORD = config.password

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)
driver.get("https://discord.com/channels/1048287921138040843")
wait = WebDriverWait(driver, 10)
email_field = wait.until(EC.presence_of_element_located((By.NAME, "email")))
email_field.send_keys(EMAIL)
password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys(PASSWORD)

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

member_list_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Show Member List']")))

member_list_button.click()

time.sleep(5)

index = 0
users = []

#before i scrape usernames i can also start first with user containers only

while True:
    user_containers = driver.find_elements(By.XPATH, f'//div[@aria-expanded="false" and @tabindex="-1" and @index="{index}" and @role="listitem"]')
    if user_containers:
        user_container = user_containers[0]
        username = user_container.find_element(By.CSS_SELECTOR, 'span[class*="username-"]').text
        users.append(username)
        index += 1
    else:
        break

print(users)

driver.quit()
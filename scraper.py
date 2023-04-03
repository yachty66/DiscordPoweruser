from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import config
import re
import clipboard

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


while True:
    user_containers = driver.find_elements(By.XPATH, f'//div[@aria-expanded="false" and @tabindex="-1" and @index="{index}" and @role="listitem"]')
    if user_containers:
        user_container = user_containers[0]
        username = user_container.find_element(By.CSS_SELECTOR, 'span[class*="username-"]').text
        avatar_img = user_container.find_element(By.CSS_SELECTOR, 'img[class*="avatar-"]')
        src = avatar_img.get_attribute('src')
        user_id_match = re.search(r'/avatars/(\d+)/', src) if src and "discord.com/assets/" not in src else None
        user_id = user_id_match.group(1) if user_id_match else None
        if user_id is None:
            user_container.click()  # Click the user container first
            time.sleep(1)
            action = webdriver.ActionChains(driver)
            action.context_click(user_container).perform()
            time.sleep(1)
            copy_id_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "user-context-devmode-copy-id")))
            copy_id_button.click()
            user_id = clipboard.paste()

        users.append((username, user_id))
        index += 1
    else:
        break


print(users)


driver.quit()
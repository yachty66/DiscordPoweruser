from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import json
import config
import re
import clipboard
import sys 

if len(sys.argv) != 3:
    print("Usage: python script_name server_id filename")
    sys.exit(1)

server_id = sys.argv[1]
filename = sys.argv[2]
output_filename = f"{filename}_{server_id}.json"
TOKEN = config.token
EMAIL = "wobbert2503@gmail.com"
PASSWORD = config.password

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/AppicationsMe/Google Chrome.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path='/Users/maxhager/Applications/AppicationsMe/chromedriver_mac_arm64/chromedriver', chrome_options=chrome_options)
url = f"https://discord.com/channels/{server_id}"
driver.get(url)
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

index = 89
users = []
#the problem is that the content is not loaded

while True:
    user_containers = driver.find_elements(By.XPATH, f'//div[@aria-expanded="false" and @tabindex="-1" and @index="{index}" and @role="listitem"]')
    print(index)
    print(user_containers)
    if user_containers:
        user_container = user_containers[0]
        username = user_container.find_element(By.CSS_SELECTOR, 'span[class*="username-"]').text
        avatar_img = user_container.find_element(By.CSS_SELECTOR, 'img[class*="avatar-"]')
        src = avatar_img.get_attribute('src')
        
        # Check if the user has an avatar
        has_avatar = src and "discord.com/assets/" not in src
        
        if has_avatar:
            user_id_match = re.search(r'/avatars/(\d+)/', src)
            user_id = user_id_match.group(1) if user_id_match else None
        else:
            user_id = None

        users.append((username, user_id))
        index += 1
    else:
        break

user_dict = {user_id: username for username, user_id in users}

with open(output_filename, 'w') as outfile:
    json.dump(user_dict, outfile)
driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, json

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        
driver.get('any url')

# Waiting for the manual login
time.sleep(30)

print("getting cookies...")

cookies = driver.get_cookies()
with open('cookies.json', 'w') as cookies_file:
    json.dump(cookies, cookies_file)

print("Cookies saved!...")
time.sleep(2)

driver.quit()
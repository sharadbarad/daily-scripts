from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time, json

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'any url'  

# Open Instagram
driver.get(url)

# May use here dynamic waiting time based on elements 
time.sleep(5)

# Load cookies from the saved JSON file
with open('cookies.json', 'r') as cookies_file:
    cookies = json.load(cookies_file)
    for cookie in cookies:
        driver.add_cookie(cookie)
        
driver.get(url)
time.sleep(30)

driver.quit()
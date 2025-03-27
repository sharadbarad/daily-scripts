import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pygame

# Set up logging configuration to suppress unnecessary info
logging.getLogger('WDM').setLevel(logging.NOTSET)

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--log-level=3")  
chrome_options.add_argument("--disable-logging")

# Automatically download and set up the latest ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL to fetch the HTML content from
url = 'url'
song_path = 'music.mp3'

def getTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Alert time: ", current_time)

def play_song(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10) 
    except Exception as e:
        print("Error:", e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

while True:
    try:
        # Fetch the content from the URL
        driver.get(url)

        # Wait until the select element is present and options are loaded
        wait = WebDriverWait(driver, 10)
        select_element = wait.until(EC.presence_of_element_located((By.ID, "id_here")))

        options = select_element.find_elements(By.TAG_NAME, 'option')

        found = False
        for option in options[1:]:  
            if 'text' in option.text.lower():
                print("Alert :", option.text)
                getTime()
                play_song(song_path)
                found = True
                break
        if not found:
            print("No alert found in the dropdown options.")
        
        time.sleep(5)
        
    except KeyboardInterrupt:
        print("Script interrupted by user. Exiting...")
        break
    except Exception as e:
        print("Something went wrong:", e)

# Close the browser
driver.quit()

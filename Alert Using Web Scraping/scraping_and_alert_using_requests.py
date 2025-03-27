import requests
from bs4 import BeautifulSoup
import pygame
from datetime import datetime
import time

# URL of the website
url = 'url_of_the_website'  
song_path='music.mp3'

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

# Fetch the HTML content from the website
while True:
    try:
        time.sleep(10)
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the dropdown menu element
        dropdown = soup.find('select', {'id': 'ddl'})
        if dropdown:
            options = dropdown.find_all('option')
            for option in options:
                if 'text' in option.text.lower():
                    print("Alert :", option.text)
                    getTime()
                    play_song(song_path)
                else:
                    print("No alert found in the dropdown options.")

        else:
            print("Dropdown not found in the HTML.")

    except KeyboardInterrupt:
        print("Script interrupted by user. Exiting...")
        break
    except Exception as e:
        print("Something went wrong:", e)

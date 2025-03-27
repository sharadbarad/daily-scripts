# 🔔 Alert System using Web Scraping

A pair of Python scripts that monitor a website for specific changes and trigger an audio alert. Created for personal use to monitor a specific website's dropdown menu changes.

---

## 📌 Overview
These scripts offer two different approaches to web scraping:
1. **Simple Method** (`scraping_and_alert_using_requests.py`): Uses `requests` and `BeautifulSoup`
2. **Advanced Method** (`scraping_and_alert_using_selenium.py`): Uses `Selenium` for JavaScript-heavy sites

## 🛠️ Setup Requirements
- Python 3.x
- Required packages: 
  ```
  pip install requests beautifulsoup4 selenium pygame webdriver-manager
  ```
- A `.mp3` file named `music.mp3` in the same directory for the alert sound

---

## ✨ Features
- Continuously monitors a specified website
- Checks dropdown menu for specific text
- Plays audio alert when target text is found
- Shows timestamp of alerts

---

## 🔧 Usage
1. Choose the appropriate script based on your needs:
   - Use `requests` script for simple websites
   - Use `selenium` script for dynamic/JavaScript-heavy sites

2. Modify these variables in the script:
   ```python
   url = 'your_target_website_url'
   song_path = 'path_to_your_alert_sound.mp3'
   ```

3. Adjust the search criteria according to your target website:
   - Modify the Structure according to your target website (Here i used id to find specific dropdown).
   - Change the search text in `'text' in option.text.lower()`

4. Run the script:
   ```
   python scraping_and_alert_using_requests.py
   # or
   python scraping_and_alert_using_selenium.py
   ```
---

## ⚠️ Note
- This project was created for personal use
- The target website URL has been removed for privacy
- Modify the scripts according to your target website's structure
- Be mindful of the website's terms of service and scraping policies (Check Robots.txt)

---

**🤝 Any issues or errors? Please raise them now.**

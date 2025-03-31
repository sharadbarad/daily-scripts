# 🚀 Daily Scripts

A collection of scripts to automate/simplify daily tasks and boost productivity.

## 📂 Projects

<details>
<summary>🔔 Alert Using Web Scraping</summary>

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
</details>

<details>
<summary>⌨️ AHK Arrowless Keyboard (CapsLock Edition)</summary>

# AHK CapsLock Navigation & Media Shortcuts

## 📌 What is AutoHotkey (AHK)?  
**AutoHotkey** is a free and open-source custom scripting language for Microsoft Windows, primarily designed to provide easy keyboard shortcuts or hotkeys, fast macro-creation and software automation to allow users of most computer skill levels to automate repetitive tasks in any Windows application.

🔗 **Download AutoHotkey**: [https://www.autohotkey.com/](https://www.autohotkey.com/)  

---

## Pain Point
My keyboard **doesn't have arrow keys** and is also **missing some media keys**, so I thought I could use Caps Lock in combination with other keys. 
I created this script to fit my needs. **You can modify this script** according to your own requirements.

---

## 🚀 How This Script Works  
Since my keyboard **doesn't have arrow keys**, I have mapped Caps Lock as a modifier key to replace arrow keys:  

| **Shortcut** | **Action** |
|-------------|-----------|
| `CapsLock + I` | Move **Up** (↑) |
| `CapsLock + K` | Move **Down** (↓) |
| `CapsLock + J` | Move **Left** (←) |
| `CapsLock + L` | Move **Right** (→) |
| `CapsLock + ;` | Move **Right** (→) |
| `CapsLock + Win + P` | Take a Screenshot (Print Screen) |
| `CapsLock + Backspace` | Delete Key |
| `CapsLock + 1` | Mute Volume |
| `CapsLock + 2` | Decrease Volume |
| `CapsLock + 3` | Increase Volume |


![IKJL](https://github.com/sharadbarad/daily-scripts/blob/main/AHK%20Arrowless%20Keyboard%20(CapsLock%20Edition)/assets/ikjl-asset.png)

👉 IKJL is somewhat similar to WSAD, which we commonly use for playing games.

---

## 🛠 How to Use This Script  

### **Option 1: Run the Script Directly**
1. **Install AutoHotkey** from [here](https://www.autohotkey.com/).  
2. Download this script and **double-click** to run it.  

### **Option 2: Convert to an EXE File**  
If you don't want to install AHK, you can convert this script into an **EXE file**:  
1. Install AutoHotkey.  
2. Right-click the `.ahk` file and select **"Compile Script"**.  
3. This will generate an `.exe` file that you can run without AutoHotkey.  

Alternatively, you can **directly download the pre-compiled `.exe` file** from the folder I have provided.

---

## 🔄 Add Script to Startup (Optional)  
To make the script run **automatically** every time you start your computer:  
1. **Press** `Win + R`, type `shell:startup`, and hit **Enter**.  
2. **Copy the `.exe` file** (or the `.ahk` script) into this folder.  
3. The script will now **run automatically** on startup!  

---

## 📂 Download  
If you don't want to compile the script yourself, you can **directly download the EXE file** from the folder I have provided.

---

## 📝 Notes  
- **Caps Lock functionality is not affected**; it still works normally for typing uppercase letters.  
- You can modify the script to **customize shortcuts** as needed.  
- To stop the script, right-click the **AHK icon in the system tray** and select **Exit**.  

💡 **Need help?** Visit the **AutoHotkey documentation**: [https://www.autohotkey.com/docs/](https://www.autohotkey.com/docs/)  

---

**Enjoy smooth navigation with Caps Lock! 🚀** 
</details>

<details>
<summary>🔄 Modified Files Tracker</summary>

# Modified Files Tracker

## 📌 Overview
This Python script helps users find files that have been modified after a specified date and time within a given directory and its subdirectories. It also provides the flexibility to exclude specific folders from the search and saves the list of modified files in a text file (`modified_files.txt`).


## 🎯 Use Cases
- **Backup Management**: Identify newly modified files to back up only what's necessary.
- **System Security**: Detect unauthorized or unexpected file modifications.

---
## 📖 How to Use
1️⃣ Run the script by executing `python modified_files_tracker.py`. </br>
2️⃣ Enter the **root folder path** where you want to search for modified files.</br>
3️⃣ Provide the **date and time** (format: `YYYY-MM-DD HH:MM:SS`) to check modifications after.</br>
4️⃣ (Optional) Enter **comma-separated folder names** to exclude from the scan.</br>
5️⃣ The script will generate `modified_files.txt` containing the list of modified files.


---
## 📂 Output
The script creates a file `modified_files.txt`, listing the names of modified files found in the directory.
</details>

<details>
<summary>🎨 Passport Size Photo 2x4 - Photoshop Script</summary>

# Passport Size Photo 2x4 - Photoshop Script

## 📌 What does it do?  
This JavaScript script is designed to be used with a Photoshop Action file (.atn). It takes a single photo in photoshop, converts it into a passport-sized image with a neat border, and arranges it in a 2x4 grid. The final Photo(2x4) can be printed on 4x6 photo paper.

---

## You give:
![Before](https://github.com/sharadbarad/daily-scripts/blob/main/Passport%20Size%20Photo%202x4%20-%20Photoshop%20Script/assets/Person%20Input%20Image.png)

## You will get:
![After](https://github.com/sharadbarad/daily-scripts/blob/main/Passport%20Size%20Photo%202x4%20-%20Photoshop%20Script/assets/2x4%20output%20image.jpg)

---

## ▶️ How to Set up this?   
* Add the Action file to photoshop From the Actions window.  
* Now place the Script (without changing name) to the `C:\Program Files\Adobe\Presets and Scripts\Script_By_SN.js`
* Set up process Done!

---

## 🛠 How to Use This Script? 
* Open Photo in photoshop 

* Photo of any person should have Transparent Background
* You can do this with photoshop or any other online web app [Adobe-Express-Online](https://www.adobe.com/in/express/feature/image/remove-background/png/transparent)

* Now select the primary color in photoshop which you want as Background in your Passport size photo.

* Now just Run that action file it will ask you how much you want to crop(it will automatically maintain the aspect ratio), once you done cropping press enter. 

* Now you get the final output of passport size images (arranged 2x4) with neat border.
</details>

<details>
<summary>🛠️ Resource Injector for EXE</summary>

# 🛠️ Inject Resources to EXE using Resource Hacker

**Here we take an example of manifest file to inject in EXE**

This Python script embeds a **manifest file** into an **EXE (executable file)** using [Resource Hacker](http://www.angusj.com/resourcehacker/) to modify Windows application behavior, such as:
- Running the EXE with **administrator privileges**.
- Enabling **DPI awareness** for high-resolution screens.
- Configuring **Windows compatibility settings**.

---

### **Install Resource Hacker**
Download and install **Resource Hacker** from the official website:  
🔗 [Download Resource Hacker](http://www.angusj.com/resourcehacker/)

### **Example of Manifest File**
Here's an example of a manifest that **forces the EXE to run as an administrator**:

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">
        <security>
            <requestedPrivileges>
                <requestedExecutionLevel level="requireAdministrator" uiAccess="false"/>
            </requestedPrivileges>
        </security>
    </trustInfo>
</assembly>
```
**Save this file as `manifest.xml`** in your working directory.


## **🚀 Run the Script**
Modify the `manifest_path` and `exe_path` inside the python script i provided:

```python
manifest_path = r"G:\manifest.xml"
exe_path = r"G:\System_manager.exe"
```

Now, run the script:

```sh
python exe_resource_injector.py
```

If successful, you'll see:

```
Manifest merged successfully.
```

---

## 📜 How It Works
The script:
1. **Locates Resource Hacker**: The script assumes it is installed in `C:\Program Files (x86)\Resource Hacker\`.
2. **Runs a Command**: It uses `subprocess` to execute a command that:
   - Opens the EXE.
   - Embeds (or replaces) the manifest.
   - Saves the updated EXE.
3. **Handles Errors**: If anything fails, an error message is displayed.

---

## ❓ Why Use a Manifest?
- **Run EXE as Administrator**: Avoids manual right-clicking → "Run as administrator".
- **Enable DPI Scaling**: Fixes blurry UI on high-resolution displays.
- **Control UAC Behavior**: Reduces unnecessary prompts.
</details>

---

**🤝 Any issues or errors? Please raise them now.**

#### ⭐ Don't forget to give this repository a star if you find it useful! ⭐
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
Here’s an example of a manifest that **forces the EXE to run as an administrator**:

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

If successful, you’ll see:

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

---

**🤝 Any issues or errors? Please raise them now.**
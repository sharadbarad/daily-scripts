import subprocess

def merge_manifest_with_exe(manifest_path, exe_path):
    resource_hacker_path = r"C:\\Program Files (x86)\\Resource Hacker\\ResourceHacker.exe"
    command = [resource_hacker_path, "-open", exe_path, "-save", exe_path, "-action", "addoverwrite", "-res", manifest_path, "-mask", "MANIFEST,1"]

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT)
        print("Manifest merged successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error merging manifest: {e.output.decode()}")

# Provide the paths to your manifest and executable files
manifest_path = r"G:\\manifest.xml"
exe_path = r"G:\\System_manager.exe"

# Merge the manifest with the executable
merge_manifest_with_exe(manifest_path, exe_path)
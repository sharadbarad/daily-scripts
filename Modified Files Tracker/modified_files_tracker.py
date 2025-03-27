import os
import datetime

def find_modified_files(root_folder, modified_after_date, excluded_folders=None):
    modified_files = set()
    
    # Convert modified_after_date to datetime object if it's a string
    if isinstance(modified_after_date, str):
        modified_after_date = datetime.datetime.strptime(modified_after_date, "%Y-%m-%d %H:%M:%S")
    
    # If excluded_folders is not provided, initialize it as an empty list
    if excluded_folders is None:
        excluded_folders = []
    
    for folder, subfolders, files in os.walk(root_folder):
        # Exclude the specified folders from being traversed
        subfolders[:] = [f for f in subfolders if f not in excluded_folders]
        
        for file in files:
            file_path = os.path.join(folder, file)
            modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            print(modified_time, modified_after_date)
            if modified_time > modified_after_date:
                modified_files.add(file)
    
    return modified_files

def main():
    root_folder = input("Enter the root folder path: ")
    modified_after_date = input("Enter the date and time (YYYY-MM-DD HH:MM:SS) to check modifications after: ")
    excluded_folders_str = input("Enter comma-separated names of folders to exclude (if any): ")
    
    # Split the excluded folder names into a list
    excluded_folders = excluded_folders_str.split(",") if excluded_folders_str else []
    
    modified_files = find_modified_files(root_folder, modified_after_date, excluded_folders)
    
    if modified_files:
        with open("modified_files.txt", "w") as f:
            for modified_file in modified_files:
                f.write(modified_file + "\n")
        print(f"Modified files have been saved to 'modified_files.txt'")
    else:
        print("No files modified after", modified_after_date)

if __name__ == "__main__":
    main()

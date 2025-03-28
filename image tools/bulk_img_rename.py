import os

def rename_images():
    folder_path = input("Enter folder path containing images: ")
    split_char = input("Enter character to split filename (default: -): ") or '-'
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.webp', '.jpeg', '.png', '.jpg')):
            
            # Get the extension
            file_ext = os.path.splitext(filename)[1]

            # Remove the extension before splitting
            name_without_ext = os.path.splitext(filename)[0]
            
            # Take the first part after splitting and add the original extension
            new_name = name_without_ext.split(split_char)[0] + file_ext
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_name}")

if __name__ == "__main__":
    rename_images()

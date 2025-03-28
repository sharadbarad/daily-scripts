from PIL import Image
import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

def resize_images():
    try:
        input_folder = input("Enter input folder path: ")
        
        output_folder = input("Enter output folder path (default: resized): ") or "resized"
        
        try:
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive numbers")
        except ValueError as e:
            print("Please enter valid numbers for width and height")
            return

        new_size = (width, height)

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if not image_files:
            print(f"No image files found in {input_folder}")
            return
            
        image_files.sort(key=natural_sort_key)
        
        for i, file_name in enumerate(image_files, start=1):
            try:
                input_path = os.path.join(input_folder, file_name)
                output_path = os.path.join(output_folder, f"{i}.jpg")
                
                img = Image.open(input_path)
                resized_img = img.resize(new_size, Image.LANCZOS)
                resized_img.save(output_path)
                print(f"Resized and saved image {i} at {output_path}")
            except Exception as e:
                print(f"Error processing {file_name}: {str(e)}")
                continue
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    resize_images()

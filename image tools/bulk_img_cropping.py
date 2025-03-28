from PIL import Image
import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', os.path.splitext(s)[0])]

def crop_images():
    input_folder = input("Enter input folder path: ")
    output_folder = input("Enter output folder path (default: cropped): ") or "cropped"
    
    while True:
        print("Enter crop coordinates (left, top, right, bottom):")
        left = int(input("Left: "))
        top = int(input("Top: "))
        right = int(input("Right: "))
        bottom = int(input("Bottom: "))
        
        if right > left and bottom > top:
            crop_area = (left, top, right, bottom)
            break
        else:
            print("Invalid coordinates. 'Right' must be greater than 'Left' and 'Bottom' must be greater than 'Top'. Please try again.")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    image_files.sort(key=natural_sort_key)
    
    for i, file_name in enumerate(image_files, start=1):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"{i}.jpg")
        
        img = Image.open(input_path)
        cropped_img = img.crop(crop_area)
        cropped_img.save(output_path)
        print(f"Cropped and saved image {i} at {output_path}")

if __name__ == "__main__":
    crop_images()

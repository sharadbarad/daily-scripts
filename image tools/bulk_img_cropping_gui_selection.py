import tkinter as tk
from tkinter import Scrollbar, Canvas
from PIL import Image, ImageTk
import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]

class CropApp:
    def __init__(self, root, image_path, aspect_ratio):
        self.root = root
        self.image_path = image_path
        self.aspect_ratio = aspect_ratio
        
        # Set preview window size
        self.preview_width = 800
        self.preview_height = 600

        # Load and scale image to fit preview
        self.original_image = Image.open(self.image_path)
        self.scale_factor = min(
            self.preview_width / self.original_image.width,
            self.preview_height / self.original_image.height
        )
        new_width = int(self.original_image.width * self.scale_factor)
        new_height = int(self.original_image.height * self.scale_factor)
        self.image = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.tk_image = ImageTk.PhotoImage(self.image)

        # Create canvas matching the scaled image size
        self.canvas = Canvas(root, width=new_width, height=new_height)
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        # Remove scrollbars since we don't need them anymore
        self.rect = None
        self.start_x = None
        self.start_y = None

        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)

        if self.rect:
            self.canvas.delete(self.rect)

        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red')

    def on_mouse_drag(self, event):
        current_x = self.canvas.canvasx(event.x)
        current_y = self.start_y + (current_x - self.start_x) / self.aspect_ratio

        self.canvas.coords(self.rect, self.start_x, self.start_y, current_x, current_y)

    def on_button_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.start_y + (self.end_x - self.start_x) / self.aspect_ratio
        self.root.quit()

    def get_crop_area(self):
        # Scale the crop coordinates back to original image size
        return (
            self.start_x / self.scale_factor,
            self.start_y / self.scale_factor,
            self.end_x / self.scale_factor,
            self.end_y / self.scale_factor
        )

def select_crop_area(image_path, aspect_ratio):
    root = tk.Tk()
    app = CropApp(root, image_path, aspect_ratio)
    root.mainloop()
    return app.get_crop_area()

def parse_aspect_ratio(ratio_str):
    if not ratio_str:
        return 16/9  # default value
    
    if '/' in ratio_str:
        width, height = map(float, ratio_str.split('/'))
        return width / height
    return float(ratio_str)

def crop_images():
    # Get user input
    input_folder = input("Enter input folder path: ")
    output_folder = input("Enter output folder path (default: cropped): ") or "cropped"
    aspect_ratio = parse_aspect_ratio(input("Enter aspect ratio (width/height, e.g. 16/9): ") or "")
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Find first image for crop area selection
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]
    if not image_files:
        print("No JPG images found in the input folder.")
        return
        
    image_files.sort(key=natural_sort_key)
    first_image_path = os.path.join(input_folder, image_files[0])
    
    print("Please select crop area in the window...")
    crop_area = select_crop_area(first_image_path, aspect_ratio)
    
    # Process all images with selected crop area
    for i, file_name in enumerate(image_files, start=1):
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, f"{i}.jpg")
        
        img = Image.open(input_path)
        cropped_img = img.crop(crop_area)
        cropped_img.save(output_path)
        print(f"Cropped and saved image {i} at {output_path}")

if __name__ == "__main__":
    crop_images()

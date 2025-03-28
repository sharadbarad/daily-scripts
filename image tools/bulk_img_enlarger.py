import os
from PIL import Image
from typing import Tuple

def get_folder_paths() -> Tuple[str, str]:
    input_folder = input("Enter input folder path: ").strip()
    output_folder = input("Enter output folder path (default: output_folder): ").strip() or 'output_folder/'
    
    if not os.path.exists(input_folder):
        raise ValueError("Input folder does not exist")
    os.makedirs(output_folder, exist_ok=True)
    return input_folder, output_folder

def resize_image(input_path: str, output_path: str, target_size: Tuple[int, int], file_format: str) -> None:
    try:
        with Image.open(input_path) as img:
            resized_img = img.resize(target_size, Image.BICUBIC)
            save_params = {'PNG': {'format': 'PNG'}, 
                         'jpg': {'format': 'JPEG', 'quality': 100}}[file_format]
            resized_img.save(output_path, **save_params)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    try:
        input_folder, output_folder = get_folder_paths()
        resize_multiplier = float(input("Enter resize multiplier (e.g., 2.0): ").strip())
        
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)
                
                with Image.open(input_path) as img:
                    file_format = 'PNG' if filename.lower().endswith('.png') else 'jpg'
                    multiplier = min(resize_multiplier, 1.5) if file_format == 'PNG' else resize_multiplier
                    target_size = (int(img.width * multiplier), int(img.height * multiplier))
                
                resize_image(input_path, output_path, target_size, file_format)
                print(f"Processed: {filename}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

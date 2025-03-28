import os
import cv2

"""
h_value -> Controls the strength of filtering (higher values for stronger filtering)
search_window_size -> Size of the search window (larger values for more smoothing)
template_window_size -> Size of the template window (smaller values for preserving more details)

"""

def nlmeans_denoise(input_path, output_path, h=10, search_window=21, template_window=7):
    """Apply Non-Local Means Denoising."""
    try:
        # Read the image
        img = cv2.imread(input_path)

        # Apply Non-Local Means Denoising
        denoised_img = cv2.fastNlMeansDenoisingColored(img, None, h=h, templateWindowSize=template_window, searchWindowSize=search_window)

        # Save the denoised image
        cv2.imwrite(output_path, denoised_img)

        print(f"Noise reduction applied to '{input_path}' and saved as '{output_path}'.")
    except Exception as e:
        print(f"Error applying noise reduction to '{input_path}':", e)

def create_directory(directory):
    """Create directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Created directory: {directory}")

def main():
    # Get input from user
    input_folder = input("Enter input folder path (default: input_folder/): ").strip() or 'input_folder/'
    output_folder = input("Enter output folder path (default: noise_reduced_images/): ").strip() or 'noise_reduced_images/'
    
    # Get denoising parameters
    try:
        h_value = int(input("Enter filtering strength (1-20, default: 12): ") or 12)
        search_window_size = int(input("Enter search window size (3-21, default: 5): ") or 5)
        template_window_size = int(input("Enter template window size (3-7, default: 3): ") or 3)
    except ValueError:
        print("Invalid input. Using default values.")
        h_value, search_window_size, template_window_size = 12, 5, 3

    # Create output folder if it doesn't exist
    create_directory(output_folder)

    # Process images
    image_count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            input_image_path = os.path.join(input_folder, filename)
            output_image_path = os.path.join(output_folder, filename)
            
            nlmeans_denoise(input_image_path, output_image_path, 
                           h=h_value, 
                           search_window=search_window_size, 
                           template_window=template_window_size)
            image_count += 1

    print(f"\nProcessing complete. {image_count} images processed.")

if __name__ == "__main__":
    main()

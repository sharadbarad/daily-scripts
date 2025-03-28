import cv2
import os

def extract_frames():
    # Get input paths from user
    video_path = input("Enter video path: ")
    output_dir = input("Enter output directory path (default: extracted_frames): ") or 'extracted_frames'
    
    # Open video first to get duration
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps

    # Get start and end times with defaults
    start_time_input = input(f"Enter start time in seconds (default: 0): ")
    end_time_input = input(f"Enter end time in seconds (default: {duration:.2f}): ")
    start_time = float(start_time_input) if start_time_input else 0
    end_time = float(end_time_input) if end_time_input else duration
    quality = int(input("Enter JPEG quality (1-100, default: 30): ") or 30)

    os.makedirs(output_dir, exist_ok=True)

    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    frame_number = start_frame
    extracted_frame_count = 0

    while frame_number <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break

        output_filename = os.path.join(output_dir, f"{extracted_frame_count + 1}.jpg")
        cv2.imwrite(output_filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
        
        extracted_frame_count += 1
        frame_number += 1

    cap.release()
    print(f"Extracted {extracted_frame_count} frames from {start_time} to {end_time} seconds.")

if __name__ == "__main__":
    extract_frames()

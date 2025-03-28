# 🖼️ Image Processing Tools

A collection of Python scripts for batch processing images, created for personal use. Feel free to modify these scripts according to your specific requirements.

---

## 🛠️ Tools Overview

<details>
<summary>🔄 Bulk Image Resizer</summary>

Batch resize images to specific dimensions while maintaining aspect ratio.
- Input: Source folder with images
- Output: Resized images in specified output folder
- Supports JPG, JPEG, PNG formats
</details>

<details>
<summary>✂️ Bulk Image Cropper</summary>

Two versions available:
1. **Simple Cropper**: Crop images using fixed coordinates
2. **GUI Cropper**: Visual interface to select crop area with aspect ratio support
- Maintains consistent cropping across all images
- Natural sorting of filenames
</details>

<details>
<summary>📝 Bulk Image Renamer</summary>

Batch rename images by splitting filenames at a specified character.
- Removes unwanted parts of filenames
- Preserves original file extensions
- Supports WEBP, JPEG, PNG, JPG formats
</details>

<details>
<summary>🔍 Bulk Image Enlarger</summary>

Scale up images to larger dimensions.
**Note**: This tool increases image size but does not enhance actual image quality.
- Supports multiple scaling factors
- Maintains aspect ratio
- High-quality bicubic interpolation
</details>

<details>
<summary>🎨 Bulk Image Noise Reduction</summary>

Reduce noise from multiple images using Non-Local Means Denoising.
- Customizable filtering strength
- Adjustable search and template window sizes
- Preserves image details while removing noise
</details>

<details>
<summary>🎞️ Video Frames Extractor</summary>

Extract frames from video files with customizable options.
- Select specific time ranges
- Adjust output quality
- Control frame extraction interval
</details>

---

## ⚠️ Notes
- These tools were created for personal use and specific requirements
- Each script can be modified to suit different needs
- Basic Python and image processing knowledge recommended for modifications

---

**🤝 Any issues or errors? Please raise them now.**

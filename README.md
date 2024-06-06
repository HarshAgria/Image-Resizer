# YoYo Image Resizer

YoYo Image Resizer is a simple Python-based tool to resize images using OpenCV and win32com.client for voice assistance. This tool prompts users for input and provides voice-guided instructions to make the image resizing process user-friendly.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)

## Features

- Resize images by specifying a percentage scale.
- Voice-guided instructions for user inputs.
- Outputs resized images in the same directory as the source image.

## Requirements

- Python 3.x
- OpenCV
- pywin32

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/yoyo-image-resizer.git
    ```

2. Navigate to the project directory:

    ```sh
    cd yoyo-image-resizer
    ```

3. Install the required dependencies:

    ```sh
    pip install opencv-python pywin32
    ```

## Usage

To use the YoYo Image Resizer, follow these steps:

1. Make sure your image file is in the same directory as the script.
2. Run the script:

    ```sh
    python resizer.py
    ```

3. Follow the voice-guided instructions:
    - Enter the image name with its extension (e.g., `image.jpg`).
    - Enter the desired name for the resized image.
    - Enter the percentage by which you want to resize the image.
  
## Folder Structure

  yoyo-image-resizer/
│
├── image_resizer.py
├── k.jpeg
├── new.png
├── README.md

- resizer.py: Main script for resizing images.
- k.jpeg: Input file
- new.png: Output file
- README.md: Project documentation.


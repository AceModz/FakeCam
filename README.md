# Fake Cam 📸

Fake Cam is a Python application that simulates a virtual camera by broadcasting images or videos from your computer. It utilizes OpenCV for video/image capture and manipulation, and PyVirtualCam to create a virtual camera device that can be used in various applications.

## Features ✨
- Upload and broadcast image files (.png, .jpg, .jpeg).
- Upload and broadcast video files (.mp4, .avi, .mov).
- Simple graphical user interface (GUI) using Tkinter.
- Play and stop buttons to control the broadcasting.
- Supports streaming to applications that recognize virtual cameras (e.g., OBS Studio).

## Requirements 🛠️
- Python 3.6+
- OpenCV (pip install opencv-python)
- PyVirtualCam (pip install pyvirtualcam)
- Tkinter (usually included in Python installations)

### Installation 🚀

1. Download the repository from GitHub or clone it using Git:
   

   - git clone https://github.com/AceModz/FakeCam.git
   - cd FakeCam
   - pip install opencv-python pyvirtualcam
   - Run in console: python main.py


### Usage 🎬

- Launch the application by running main.py.
- Click on the "Upload File" button to select an image or video file.
- Click "Play" to start broadcasting the selected file.
- Click "Stop" to stop broadcasting.

### Notes ℹ️
**Virtual Camera: Ensure you have OBS Studio or another application that supports virtual cameras installed to use the broadcasted feed.**
**File Formats: Supported formats include .png, .jpg, .jpeg for images and .mp4, .avi, .mov for videos.**

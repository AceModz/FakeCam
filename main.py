import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import pyvirtualcam
from pyvirtualcam import PixelFormat
import threading
import os

class FakeCamApp:
    def __init__(self, root):
        os.system('cls')  # Clear the console on startup

        self.root = root
        self.root.title("Fake Cam")
        self.root.geometry("500x300")
        self.root.configure(bg="#2e2e2e")  # Set background color

        self.file_path = None
        self.cap = None
        self.running = False

        # Create title label
        self.title_label = tk.Label(root, text="Fake Cam", font=("Helvetica", 24), fg="white", bg="#2e2e2e")
        self.title_label.pack(pady=20)

        # Create upload button
        self.upload_btn = tk.Button(root, text="Upload File", command=self.upload_file, width=20, font=("Helvetica", 14), bg="#4caf50", fg="white")
        self.upload_btn.pack(pady=10)

        # Create play button
        self.play_btn = tk.Button(root, text="Play", command=self.start_broadcast, width=20, font=("Helvetica", 14), bg="#2196f3", fg="white")
        self.play_btn.pack(pady=10)

        # Create stop button
        self.stop_btn = tk.Button(root, text="Stop", command=self.stop_broadcast, width=20, font=("Helvetica", 14), bg="#f44336", fg="white")
        self.stop_btn.pack(pady=10)
        
    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov"), ("Image files", "*.png;*.jpg;*.jpeg")])
        if self.file_path:
            print(f"File selected: {self.file_path}")
        else:
            messagebox.showerror("Error", "No file selected")

    def start_broadcast(self):
        if self.file_path:
            self.running = True
            self.broadcast_thread = threading.Thread(target=self.broadcast)
            self.broadcast_thread.start()
        else:
            print("Please upload a file first.")
            
    def stop_broadcast(self):
        self.running = False
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None
        print("Broadcast stopped.")

    def broadcast(self):
        if self.file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            self.broadcast_image()
        else:
            self.broadcast_video()
            
    def broadcast_image(self):
        img = cv2.imread(self.file_path)
        height, width, _ = img.shape
        with pyvirtualcam.Camera(width, height, fps=20, fmt=PixelFormat.BGR) as cam:
            print(f"Using virtual camera: {cam.device}")
            while self.running:
                cam.send(img)
                cam.sleep_until_next_frame()

    def broadcast_video(self):
        self.cap = cv2.VideoCapture(self.file_path)
        if not self.cap.isOpened():
            print("Error: Cannot open video file.")
            self.cap = None
            self.running = False
            return
        
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        with pyvirtualcam.Camera(width, height, fps=20, fmt=PixelFormat.BGR) as cam:
            print(f"Using virtual camera: {cam.device}")
            while self.running and self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break
                cam.send(frame)
                cam.sleep_until_next_frame()
        if self.cap and self.cap.isOpened():
            self.cap.release()
            self.cap = None

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeCamApp(root)
    root.mainloop()

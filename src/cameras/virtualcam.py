import cv2
import pyvirtualcam
import numpy as np
import threading


class VirtualCam:

    def __init__(self, width: int, height: int):
        self.frame = np.zeros((int(height), int(width), 3), np.uint8)  # RGB

        self.running = True
        self.thread = threading.Thread(target=self.show_cam, args=(width, height))
        self.thread.start()

    def set_frame(self, frame):
        self.frame = frame

    def quit(self):
        self.running = False
        self.thread.join()

    def show_cam(self, width, height):
        with pyvirtualcam.Camera(
                width=int(width),
                height=int(height),
                fps=30, device="/dev/video2",
                fmt=pyvirtualcam.PixelFormat.BGR) as cam:

            print(f'Using virtual camera: {cam.device}')
            while self.running:
                cam.send(self.frame)
                cam.sleep_until_next_frame()

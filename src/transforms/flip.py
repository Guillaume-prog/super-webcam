from src.transforms.base import BaseTf
import numpy as np
import cv2

import threading
import time


def start_thread(cb, total_time):
    threading.Thread(target=cb, args=[total_time]).start()


def rotate_image(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result


class FlipTf(BaseTf):

    def __init__(self):
        self.flip_x = False
        self.flip_y = False
        self.windmill = False

        self.angle = 0

    def spin(self, total_time):
        step = 1
        step_time = total_time / (360/step)
        for i in range(0, 360, step):
            self.angle = i
            time.sleep(step_time)
        self.angle = 0

    def on_key(self, key: chr):
        if key == 'f':
            self.flip_x = not self.flip_x
        elif key == 'g':
            self.flip_y = not self.flip_y
        elif key == 'h':
            self.windmill = not self.windmill

    def tf(self, img):
        if self.flip_x and self.flip_y:
            img = cv2.flip(img, -1)
        elif self.flip_x:
            img = cv2.flip(img, 1)
        elif self.flip_y:
            img = cv2.flip(img, 0)

        img = rotate_image(img, -self.angle)

        if self.windmill:
            start_thread(self.spin, 0.7)
            self.windmill = False

        return img

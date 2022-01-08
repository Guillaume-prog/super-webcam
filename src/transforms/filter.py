from src.transforms.base import BaseTf
import numpy as np
import cv2

import threading
import time


class FilterTf(BaseTf):

    def __init__(self):
        self.bw = False

    def on_key(self, key: chr):
        if key == 'b':
            self.bw = not self.bw

    def tf(self, img):
        if self.bw:
            grayscale = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img = np.zeros_like(img)
            img[:, :, 0] = grayscale
            img[:, :, 1] = grayscale
            img[:, :, 2] = grayscale

        return img

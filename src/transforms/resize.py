from .base import BaseTf
import cv2


class ResizeTf(BaseTf):

    def __init__(self, width_ratio, height_ratio):
        self.ratio = width_ratio / height_ratio

    def on_key(self, key: chr):
        pass

    def tf(self, img):
        width = img.shape[1]
        height = img.shape[0]

        new_height = int(width / self.ratio)

        start_y = int((height - new_height) / 2)
        end_y = int((height + new_height) / 2)

        img = img[start_y:end_y, 0:width]

        return img

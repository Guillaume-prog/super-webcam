import cv2
from .base import BaseTf


class ZoomTf(BaseTf):

    def __init__(self, factor: float):
        self.zoom_lvl = 0
        self.zoom_factor = factor

    def on_key(self, key: chr):
        if key == 'a':
            self.zoom_lvl = 1
        elif key == 'z':
            self.zoom_lvl = 2
        elif key == 's':
            self.zoom_lvl = 0
        elif key == 'e':
            self.zoom_lvl = 10

    def tf(self, img):
        if self.zoom_lvl == 0:
            return img

        width = img.shape[1]
        height = img.shape[0]
        to_zoom = self.zoom_lvl * self.zoom_factor

        def get_corner(side: int):
            # Get the new coordinates on a reduced rectangle
            get_new = lambda a: int(a / 2 * (1 + side / to_zoom))
            return get_new(width), get_new(height)

        top_left = get_corner(-1)
        bottom_right = get_corner(1)

        cropped_section = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        resized_image = cv2.resize(cropped_section, (width, height))

        return resized_image

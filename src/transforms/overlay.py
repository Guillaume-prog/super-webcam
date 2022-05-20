from .base import BaseTf
import cv2


class OverlayTf(BaseTf):

    def __init__(self):
        self.show_brb = False
        self.brb_img = cv2.imread("/var/code/webcam-tools/src/assets/brb.jpeg", cv2.IMREAD_COLOR)

    def on_key(self, key: chr):
        if key == 'w':
            self.show_brb = not self.show_brb

    def tf(self, img):
        if self.show_brb:
            img = cv2.resize(self.brb_img, (img.shape[1], img.shape[0]))

        return img

import cv2
from src.transforms import *
from src.cameras.virtualcam import VirtualCam


class Camera:

    ZOOM_FACTOR = 1.5

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self.vcam = VirtualCam(self.cam.get(3), self.cam.get(4))

        self.running = True

        self.tfs = [ZoomTf(1.5), FaceTf(), FlipTf(), FilterTf()]

    def quit(self):
        self.cam.release()
        self.vcam.quit()
        cv2.destroyAllWindows()

    def main_loop(self):
        success, img = self.cam.read()
        self.manage_events()

        for tf in self.tfs:
            img = tf.tf(img)

        cv2.imshow("Super Webcam", img)
        self.vcam.set_frame(img)

    def manage_events(self):
        key = chr(cv2.waitKey(1) & 0xFF)

        if key == 'q':
            self.running = False

        for tf in self.tfs:
            img = tf.on_key(key)

import cv2
from src.transforms import *
from src.cameras.virtualcam import VirtualCam


class Camera:

    ZOOM_FACTOR = 1.5

    def get_sources(self):
        pass

    def __init__(self, ratio_x, ratio_y):
        self.cam = cv2.VideoCapture(0)

        width = int(self.cam.get(3))
        height = int(width / (ratio_x / ratio_y))
        print(width, height)
        self.vcam = VirtualCam(width, height)

        self.running = True

        self.tfs = [ResizeTf(ratio_x, ratio_y), ZoomTf(1.5), FaceTf(), FlipTf(), FilterTf(), OverlayTf()]

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

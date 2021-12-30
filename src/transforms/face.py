import cv2
from cvzone.FaceDetectionModule import FaceDetector

from .base import BaseTf


class FaceTf(BaseTf):

    def __init__(self):
        self.detector = FaceDetector()
        self.tracking = False

    def on_key(self, key: chr):
        if key == 't':
            self.tracking = not self.tracking

    def tf(self, img):
        if not self.tracking:
            return img

        img, bboxs = self.detector.findFaces(img)

        if bboxs:
            # bboxInfo - "id","bbox","score","center"
            center = bboxs[0]["center"]
            cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

        return img

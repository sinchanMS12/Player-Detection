"""

** coded by Sathwik,Sourav,Sinchan,pratyush  on 19/10/2024 **
** God Speed **
** May all beings be Happy,Peaceful,Liberated **

"""
import cv2


class SimplePreprocessor:
    def __init__(self, width, height, inter=cv2.INTER_AREA):
        self.width = width
        self.height = height
        self.inter = inter

    def preprocess(self, image):
        return cv2.resize(image, (self.width, self.height), interpolation=self.inter)

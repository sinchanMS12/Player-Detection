"""

** coded by Sathwik,Sourav,Sinchan,pratyush  on 19/10/2024 **
** God Speed **
** May all beings be Happy,Peaceful,Liberated **

"""
from keras.preprocessing.image import img_to_array


class ImageToArrayPreprocessor:
    def __init__(self, dataFormat=None):
        self.dataFormat = dataFormat

    def preprocess(self, image):
        return img_to_array(image, data_format=self.dataFormat)

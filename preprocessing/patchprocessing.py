"""
** coded by Sathwik,Sourav,Sinchan,pratyush  on 19/10/2024 **
** God Speed **
** May all beings be Happy,Peaceful,Liberated **

"""
from sklearn.feature_extraction.image import extract_patches_2d


class patchProcessor:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def preprocess(self, image):
        return extract_patches_2d(image, self.height, self.width, max_patches=1)[0]

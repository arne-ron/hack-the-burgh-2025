from PIL import Image
import numpy as npm


# Normalizes the values in an image array to a range of 20 to 37
def normalize(image) -> Image:
    newImageArray = npm.zeros((image.shape[0], image.shape[1]))
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            newImageArray[i][j] = (13 * (image[i][j]-20)) # between 0 and 255?
    return newImageArray
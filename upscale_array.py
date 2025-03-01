from PIL import Image
import numpy as np



def upscaleArray(arr):
    factor = 3
    newArray = []
    for x in range(arr.shape[0] * factor):
        newArray.append([])
        for y in range(arr.shape[1 * factor]):
            newArray[x].append(arr[x//factor + 1, y//factor])

    return np.array(newArray, dtype=np.uint8)

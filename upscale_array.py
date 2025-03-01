from PIL import Image
import numpy as np
def upscaleArray(arr):
    newArray = []
    for i in range(len(arr)):
        for j in range(3):
            row = []
            for k in range (len(arr[i])):
                row.extend([arr[i][k]]*3)
            newArray.append(row)
    return newArray
array = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]

input_path_sat_1 = "data/20230215-SE2B-CGG-GBR-MS3-L3-RGB-preview.jpg"
sat_1 = Image.open(input_path_sat_1)

sat_1_small = sat_1.resize((100, 100))

array = np.array(sat_1_small)
newImage = upscaleArray(array)
# sImg = Image.fromarray(newImage)
# sImg.show() 
print(array)
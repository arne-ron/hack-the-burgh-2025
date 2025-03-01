from PIL import Image
import numpy as np

# def 
#     newArray = []
#     for i in range(len(arr)):  # Iterate over rows
#         for _ in range(3):  # Repeat each row 3 times (vertical scaling)
#             row = []
#             for k in range(len(arr[i])):  # Iterate over columns
#                 row.extend([arr[i][k]] * 3)  # Repeat each [R, G, B] triplet 3 times (horizontal scaling)
#             newArray.append(row)  # Append the expanded row
#     return np.array(newArray, dtype=np.uint8)  # Convert back to NumPy array



def upscaleArray(arr):
    factor = 3
    newArray = []
    for x in range(arr.shape[0] * factor):
        newArray.append([])
        for y in range(arr.shape[1 * factor]):
            newArray[x].append(arr[x//factor + 1, y//factor])

    return np.array(newArray, dtype=np.uint8)

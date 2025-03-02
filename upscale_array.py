import numpy as np
import matplotlib.pyplot as plt



def upscaleArray(arr, directionField, threshold):
    factor = 10
    newArray = []
    histogramList = []
    for x in range(arr.shape[0] * factor):
        newArray.append([])
        for y in range(arr.shape[1] * factor):
            direction = directionField[x,y]
            offset=[0,0]

            if direction[0] > threshold:
                offset += [1,0]
            elif direction[0] < -threshold:
                offset += [-1,0]
            if direction[1] > threshold:
                offset += [0,1]
            elif direction[1] < -threshold:
                offset += [0,-1]

            newArray[x].append(arr[x//factor + offset[0], y//factor + offset[1]])
            histogramList.append(direction[0] * direction[0] + direction[1] * direction[1])
    
    # plt.hist(histogramList, bins=100, density=True, alpha=0.6, color='g', log=True)
    # plt.xlabel('squared dist')
    # plt.ylabel('Amount')
    # plt.title('Density Distribution of magnitudes')
    # plt.show()
    
    return np.array(newArray, dtype=np.uint8)

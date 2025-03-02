from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



def upscaleArray(arr, directionField):
    factor = 10
    newArray = []
    offsets = []
    for x in range(arr.shape[0] * factor):
        newArray.append([])
        for y in range(arr.shape[1] * factor):
            direction = directionField[x,y]
            offset=[0,0]
            if direction[0] > 1:
                offset += [1,0]
                
            elif direction[0] < -1:
                offset += [-1,0]
                
            if direction[1] > 1:
                offset += [0,1]
                
            elif direction[1] < -1:
                offset += [0,-1]


            
            
            
            
            
            newArray[x].append(arr[x//factor + offset[0], y//factor + offset[1]])
            offsets.append(offset[0] + offset[1])
    plt.hist(offsets, bins=20, density=True, alpha=0.6, color='g')
    plt.xlabel('Offset Value')
    plt.ylabel('Density')
    plt.title('Density Distribution of Offsets')
    plt.show()
    return np.array(newArray, dtype=np.uint8)

import numpy as np
import matplotlib.pyplot as plt

from clamp import clamp



def upscaleArray(arr, directionField, depthmap, threshold):
    factor = 10
    newArray = []
    histogramList = []
    max_pixel_step = 5
    for x in range(arr.shape[0] * factor // 2):
        newArray.append([])
        for y in range((arr.shape[1] * factor // 3) + 500):
            if y < 500:
                continue
            # pos = find_nearest_edge(x, y, directionField, threshold)
            # direction = directionField[pos[0], pos[1]]
            direction = directionField[x,y]
            offset=[0,0]
            
            delta = depthmap[clamp(x + direction[0], 0, len(depthmap) - 1), clamp(y + direction[1],0,len(depthmap) - 1)] - depthmap[x, y]
            if delta > 0.5:
                direction = -direction

            step = int(clamp(mag_sq(direction)/10, 1, max_pixel_step))

            if direction[0] > threshold:
                offset[0] = offset[0] + step
            elif direction[0] < -threshold:
                offset[0] = offset[0] - step
            if direction[1] > threshold:
                offset[1] = offset[1] - step
            elif direction[1] < -threshold:
                offset[1] = offset[1] + step
                        
            
            color = arr[clamp(x//factor + offset[0],0,len(arr)-1), clamp(y//factor + offset[1],0,len(arr)-1)]
            newArray[x].append(color)
                
    

    
    return np.array(newArray, dtype=np.uint8)



def find_nearest_edge(x, y, directionField, threshold):
    i = 1
    while (i <= 30): 
        try:
            current = directionField[x+i, y]
            if mag_sq(current) > threshold:
                return (x+i, y)
            current = directionField[x-i, y]
            if mag_sq(current) > threshold:
                return (x-i, y)
            current = directionField[x, y+i]
            if mag_sq(current) > threshold:
                return (x, y+i)
            current = directionField[x, y-i]
            if mag_sq(current) > threshold:
                return (x, y-i)
        except:
            pass
        i += 1
    return (x, y)



def mag_sq(vec):
    return vec[0]*vec[0] + vec[1]*vec[1]
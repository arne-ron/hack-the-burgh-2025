import numpy as np
import matplotlib.pyplot as plt

from utils import clamp, mag_sq


# Perform the advanced upscale of the array using a gradient field and depthmap
# The threshold is used to determine which pixel should be moved (a value of 10 is recommended for housing areas)
# The algorithm is more thoroughly explained in the presentation in the Repo
# arr: numpy array - The array to upscale
# gradient_field: numpy array - The gradient field of the array, 10 times larger than array
# depthmap: numpy array - The depthmap of the area, 10 times larger than array
# threshold: int - The threshold for moving pixels in meters d/dx
def upscale_array(arr, gradient_field, depthmap, threshold):
    factor = 10 # Hardcoded for now. Might not be working properly for other values
    max_pixel_step = 4

    storage_arr = []
    for x in range(arr.shape[0] * factor):
        storage_arr.append([])
        for y in range(arr.shape[1] * factor):
            direction = gradient_field[x,y]
            offset=[0,0]
            
            delta = depthmap[clamp(x + direction[0], 0, len(depthmap) - 1), clamp(y + direction[1],0,len(depthmap) - 1)] - depthmap[x, y]
            if delta > 0.5:
                direction = -direction

            step = int(clamp(mag_sq(direction)/80, 1, max_pixel_step))

            if direction[0] > threshold:
                offset[0] = offset[0] - step
            elif direction[0] < -threshold:
                offset[0] = offset[0] + step
            if direction[1] > threshold:
                offset[1] = offset[1] - step
            elif direction[1] < -threshold:
                offset[1] = offset[1] + step
                        
            
            color = arr[clamp(x//factor + offset[0],0,len(arr)-1), clamp(y//factor + offset[1],0,len(arr)-1)]
            storage_arr[x].append(color)
                
    
    return np.array(storage_arr, dtype=np.uint8)



# Not currently in use
# All approaches with this did not yield better results than the current implementation
# while heavily impacting performance
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

from PIL import Image
import numpy as np
import time

from run_kernel import run_kernel1D_arr
from kernels import xSobel, ySobel, ySobelBig



input_path_LiDAR_1 = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'

start_time = time.time()
print("Caching start...")

ySobelBig = np.array(ySobelBig)

# Normal Resolution caching of the gradient
LiDAR_1 = Image.open(input_path_LiDAR_1)
arr = np.array(LiDAR_1)
red = run_kernel1D_arr(arr, ySobelBig.transpose())
green = run_kernel1D_arr(arr, ySobelBig)

gradientArr = np.dstack((red, green, np.zeros(LiDAR_1.size))).astype(np.uint8)


gradient = Image.fromarray(gradientArr, "RGB")
gradient.save("cache/gradient_full.tiff")



# Normal Resolution caching of the gradient
LiDAR_1_reduced = LiDAR_1.resize((1000, 1000))
arr_reduced = np.array(LiDAR_1_reduced)
red_reduced = run_kernel1D_arr(arr_reduced, ySobelBig.transpose())
green_reduced = run_kernel1D_arr(arr_reduced, ySobelBig)

gradientArr_reduced = np.dstack((red_reduced, green_reduced, np.zeros(LiDAR_1_reduced.size))).astype(np.uint8)


gradient_reduced = Image.fromarray(gradientArr_reduced, "RGB")
gradient_reduced.save("cache/gradient_reduced.tiff")

print("Caching successful in " + str(time.time() - start_time) + " seconds!")
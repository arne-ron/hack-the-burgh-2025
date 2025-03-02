from PIL import Image
import numpy as np

from run_kernel import run_kernel1D_arr
from kernels import xSobel, ySobel, testKernels


input_path_LiDAR_1 = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'
LiDAR_1 = Image.open(input_path_LiDAR_1)


print("Caching start...")

# Normal Resolution caching of the gradient
LiDAR_1_reduced = LiDAR_1.resize((1000, 1000))
arr_reduced = np.array(LiDAR_1_reduced)
for n in range(len(testKernels)):
    kernel = np.array(testKernels[n])
    red_reduced = run_kernel1D_arr(arr_reduced, kernel)
    green_reduced = run_kernel1D_arr(arr_reduced, kernel.transpose())

    gradientArr_reduced = np.dstack((red_reduced, green_reduced, np.zeros(LiDAR_1_reduced.size))).astype(np.uint8)


    gradient_reduced = Image.fromarray(gradientArr_reduced, "RGB")
    gradient_reduced.save("cache/testkernel" + str(n) + ".tiff")

print("Caching successful!")
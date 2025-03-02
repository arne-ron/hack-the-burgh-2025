from PIL import Image
 
import numpy as np
import time


from run_kernel import run_kernelRGB, run_kernel1D, run_kernel1D_arr
from kernels import xSobel, ySobel, ySobelBig
from upscale_array import upscaleArray, upscaleArrayNew
from clamp import clamp


RUN_REDUCED = False


# Original satelite images with 10m x 10m accuracy
input_path_sat_1 = "data/20230215-SE2B-CGG-GBR-MS3-L3-RGB-preview.jpg"
input_path_sat_2 = 'data/20230215-SE2B-CGG-GBR-MS3-L3-NRG-preview.jpg'

input_path_LiDAR_1 = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'

gradient_cache = ''
if RUN_REDUCED:
    gradient_cache = 'cache/gradient_reduced.tiff'
else:
    gradient_cache = 'cache/gradient_full.tiff'

output_path_sat = 'out/upscaled.tif'




sat_1 = Image.open(input_path_sat_1)
# sat_2 = Image.open(input_path_sat_2)
LiDAR = Image.open(input_path_LiDAR_1)
if RUN_REDUCED:
    sat_1 = sat_1.resize((100, 100))
    # sat_2 = sat_2.resize((100, 100))

gradient = Image.open(gradient_cache)






start_time = time.time()
print("Running...")


# Upscale the image - from 1 pixel to 10 pixels
array = np.array(sat_1)
gradient_arr = np.array(gradient)
new_image_arr = upscaleArrayNew(array, gradient_arr, np.array(LiDAR), threshold=5)
img_res = Image.fromarray(new_image_arr, "RGB")
img_res.save(output_path_sat)
img_res.show()


end_time = time.time()
print(f"Done in {end_time - start_time} seconds")

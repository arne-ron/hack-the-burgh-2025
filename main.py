from PIL import Image
 
import numpy as np
import time


from run_kernel import run_kernelRGB, run_kernel1D, run_kernel1D_arr
from kernels import xSobel, ySobel
from upscale_array import upscaleArray


RUN_REDUCED = True


# Original satelite images with 10m x 10m accuracy
input_path_sat_1 = "data/20230215-SE2B-CGG-GBR-MS3-L3-RGB-preview.jpg"
input_path_sat_2 = 'data/20230215-SE2B-CGG-GBR-MS3-L3-NRG-preview.jpg'

gradient_cache = ''
if RUN_REDUCED:
    gradient_cache = 'cache/gradient_reduced.tiff'
else:
    gradient_cache = 'cache/gradient_full.tiff'

output_path_sat = 'out/upscaled.tif'




sat_1 = Image.open(input_path_sat_1)
# sat_2 = Image.open(input_path_sat_2)
if RUN_REDUCED:
    sat_1 = sat_1.resize((100, 100))
    # sat_2 = sat_2.resize((100, 100))

gradient = Image.open(gradient_cache)




start_time = time.time()
print("Running...")




# Upscale the image - from 1 pixel to 10 pixels
array = np.array(sat_1)
gradient_arr = np.array(gradient)
new_image_arr = upscaleArray(array, gradient_arr, threshold=5)
img_res = Image.fromarray(new_image_arr, "RGB")  
img_res.show()
sat_1.show()
img_res.save(output_path_sat)



end_time = time.time()
print(f"Done in {end_time - start_time} seconds")

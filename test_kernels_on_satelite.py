from PIL import Image
 
import numpy as np
import time


from run_kernel import run_kernelRGB, run_kernel1D, run_kernel1D_arr
from kernels import xSobel, ySobel
from upscale_array import upscaleArray
from clamp import clamp

RUN_REDUCED = False


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










start_time = time.time()
array = np.array(sat_1)
print("Running...")
for n in range(3):
    gradient = Image.open("cache/testkernel" + str(n) + ".tiff")


    gradient_arr = np.array(gradient)
    new_image_arr = upscaleArray(array, gradient_arr, threshold=5)
    img_res = Image.fromarray(new_image_arr, "RGB")  
    img_res.show()
    img_res.save(output_path_sat + str(n) + ".tiff")



end_time = time.time()
print(f"Done in {end_time - start_time} seconds")

from PIL import Image
 
import numpy as np


from run_kernel import run_kernelRGB, run_kernel1D, run_kernel1D_arr
from kernels import xSobel, ySobel
from upscale_array import upscaleArray


# Original satelite images with 10m x 10m accuracy
input_path_sat_1 = "data/20230215-SE2B-CGG-GBR-MS3-L3-RGB-preview.jpg"
input_path_sat_2 = 'data/20230215-SE2B-CGG-GBR-MS3-L3-NRG-preview.jpg'

# Original LiDAR images with 1m x 1m accuracy
input_path_LiDAR_1 = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'
input_path_LiDAR_2 = "data/20230215_SE2B_CGG_GBR_MS4_L3_BGRN.tif"

output_path_sat = 'out/upscaled.tif'


sat_1 = Image.open(input_path_sat_1)
sat_2 = Image.open(input_path_sat_2)

LiDAR_1 = Image.open(input_path_LiDAR_1)
# LiDAR_2 = Image.open(input_path_LiDAR_2)


sat_1_small = sat_1.resize((100, 100))
LiDAR_1_small = LiDAR_1.resize((1000, 1000))





print("Running...")


arr = np.array(LiDAR_1_small)
red = run_kernel1D_arr(arr, xSobel)
green = run_kernel1D_arr(arr, ySobel)

gradientArr = np.dstack((red, green, np.zeros(LiDAR_1_small.size))).astype(np.uint8)




gradient = Image.fromarray(gradientArr, "RGB")
gradient.show()


#Upscale the image - from 1 pixel to 10 pixels
array = np.array(sat_1_small)
newImage = upscaleArray(array, gradientArr)
print(newImage)
sImg = Image.fromarray(newImage, "RGB")  
sImg.show()




print("Done")

from PIL import Image
import numpy as np
import time


from landuse_objects import landuse_objects


from get_gradient import get_gradient
from upscale_array import upscale_array


# Uses a lower resolution image for faster execution
RUN_REDUCED = False


# Original satelite images with 10m x 10m accuracy, provided by viridien, sourced from ESA
input_path_sat = "data/20230215-SE2B-CGG-GBR-MS3-L3-RGB-preview.jpg"
input_path_sat_2 = 'data/20230215-SE2B-CGG-GBR-MS3-L3-NRG-preview.jpg'
# Original LiDAR images with 1m x 1m accuracy
input_path_LiDAR = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'
input_path_normalized_LiDAR = 'data/normalizedLiDAR.PNG'

input_path_LiDAR_1 = 'data/DSM_TQ0075_P_12757_20230109_20230315.tif'


output_path_sat = 'upscaled.tif'

normalized_LiDAR = Image.open(input_path_normalized_LiDAR)







start_time = time.time()
sat_img = Image.open(input_path_sat)
sat_2_img = Image.open(input_path_sat_2)
LiDAR_img = Image.open(input_path_LiDAR)
if RUN_REDUCED:
    sat_img = sat_img.resize((100, 100))
    LiDAR_img = LiDAR_img.resize((1000,1000))
array = np.array(sat_img)
LiDAR_arr = np.array(LiDAR_img)

gradient_arr = get_gradient(LiDAR_arr)

print("Processing...")
new_image_arr = upscale_array(array, gradient_arr, LiDAR_arr, threshold=10)
img_res = Image.fromarray(new_image_arr, "RGB")
img_res.save(output_path_sat)
img_res.show()
end_time = time.time()
print(f"Done in {end_time - start_time} seconds")


print("Analyzing...")
landuseLiDARImage = np.array(normalized_LiDAR.resize((1000,1000)))
landuseSatImage = np.array(sat_img.resize((1000,1000)))
landuseRedImage = np.array(sat_2_img.resize((1000,1000)))

landuse_objects(landuseLiDARImage, landuseSatImage, landuseRedImage)
print("Program done")




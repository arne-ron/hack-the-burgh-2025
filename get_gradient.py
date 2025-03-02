import numpy as np
import time

from run_kernel import run_kernel1D_arr
from kernel import ySobelBig




# Calculate the gradient of the array in x and y direction and returns this as a 2D-array of triples
# The first two values of the triple are the gradient in x and y direction, the third value is 0
def get_gradient(arr):
    print("Calculating gradient...")
    start_time = time.time()

    kernel = np.array(ySobelBig)

    red = run_kernel1D_arr(arr, kernel.transpose())
    green = run_kernel1D_arr(arr, kernel)

    gradientArr = np.dstack((red, green, np.zeros(arr.shape))).astype(np.uint8)

    print("Calculation successful in " + str(time.time() - start_time) + " seconds!")
    return gradientArr

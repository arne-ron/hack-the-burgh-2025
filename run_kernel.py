from PIL import Image
import numpy as npm


# Currently not working properly
def run_kernelRGB(img: Image, kernel) -> float:
    img_arr = npm.array(img)

    imageHeight = img.size[0]
    imageWidth = img.size[1]

    kernelHeight = kernel.shape[0]
    kernelWidth = kernel.shape[1]

    noOfChannels = 3

    channel_vals = npm.array([npm.zeros((imageHeight, imageWidth)) for _ in range(noOfChannels)])

    def put_zeroes(i, j):
        for k in range(noOfChannels):
            channel_vals[k, i, j] = 0
    

    for i in range(imageHeight):
        for j in range(imageWidth):
            if (j == 0 or j == imageWidth - 1) or (i == 0 or i == imageHeight - 1):
                put_zeroes(i, j)
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            for k in range(noOfChannels):
                val = npm.sum(window[:,:,k] * kernel)
                channel_vals[k,i , j] = min(256, max(0, val))
    
    print(channel_vals.shape)
    stacked_array = npm.dstack(channel_vals).astype(npm.uint8)
    print(stacked_array.shape)
    return_img = Image.fromarray(stacked_array, mode='RGB')
    return return_img


# Loops the kernel over the image and returns the resulting image
# img: Image - the image to apply the kernel to. It must be a grayscale image
# kernel: numpy array - the kernel to apply to the image
# returns: Image - the resulting image
def run_kernel1D(img: Image, kernel) -> float:
    img_arr = npm.array(img)

    imageHeight = img.size[0]
    imageWidth = img.size[1]

    kernelHeight = kernel.shape[0]
    kernelWidth = kernel.shape[1]


    vals = npm.zeros((imageHeight, imageWidth))
    

    for i in range(imageHeight//2):
        for j in range(imageWidth//2):
            if (j < kernelWidth // 2 or j >= imageWidth - kernelWidth // 2) or (i < kernelHeight // 2 or i >= imageHeight - kernelHeight // 2):
                vals[i, j] = 0
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            val = npm.sum(window * kernel)
            vals[i , j] = min(256, max(0, val))
    

    return_img = Image.fromarray(vals)
    return return_img


# Loops the kernel over the array and returns the resulting array
# img_arr: numpy array - the image array to apply the kernel to. It must have a size of (height, width)
# kernel: numpy array - the kernel to apply to the image
# returns: numpy array - the resulting image array
def run_kernel1D_arr(img_arr, kernel) -> float:
    imageHeight = img_arr.shape[0]
    imageWidth = img_arr.shape[1]

    kernelHeight = kernel.shape[0]
    kernelWidth = kernel.shape[1]


    vals = npm.zeros((imageHeight, imageWidth))
    

    for i in range(imageHeight):
        for j in range(imageWidth):
            if (j < kernelWidth // 2 or j >= imageWidth - kernelWidth // 2) or (i < kernelHeight // 2 or i >= imageHeight - kernelHeight // 2):
                vals[i, j] = 0
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            val = npm.sum(window * kernel)
            vals[i , j] = min(256, max(0, val))
    
    return vals
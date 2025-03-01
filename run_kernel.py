from PIL import Image
import numpy as npm


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
    

    for i in range(imageHeight//2):
        for j in range(imageWidth//2):
            if (j == 0 or j == imageWidth - 1) or (i == 0 or i == imageHeight - 1):
                put_zeroes(i, j)
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            for k in range(noOfChannels):
                val = npm.sum(window[:,:,k] * kernel)
                channel_vals[k,i , j] = min(256, max(0, val))
    
    print(channel_vals.shape)
    stacked_array = npm.dstack(channel_vals)
    print(stacked_array.shape)
    return_img = Image.fromarray(stacked_array, mode='RGB')
    return return_img






def run_kernel1D(img: Image, kernel) -> float:
    img_arr = npm.array(img)


    imageHeight = img.size[0]
    imageWidth = img.size[1]

    kernelHeight = kernel.shape[0]
    kernelWidth = kernel.shape[1]


    vals = npm.zeros((imageHeight, imageWidth))


    def put_zeroes(i, j):
        vals[i, j] = 0
    

    for i in range(imageHeight//2):
        for j in range(imageWidth//2):
            if (j == 0 or j == imageWidth - 1) or (i == 0 or i == imageHeight - 1):
                put_zeroes(i, j)
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            val = npm.sum(window * kernel)
            vals[i , j] = min(256, max(0, val))
    

    return_img = Image.fromarray(vals)
    return return_img


def run_kernel1D_arr(img_arr, kernel) -> float:


    imageHeight = img_arr.shape[0]
    imageWidth = img_arr.shape[1]

    kernelHeight = kernel.shape[0]
    kernelWidth = kernel.shape[1]


    vals = npm.zeros((imageHeight, imageWidth))


    def put_zeroes(i, j):
        vals[i, j] = 0
    

    for i in range(imageHeight//2):
        for j in range(imageWidth//2):
            if (j == 0 or j == imageWidth - 1) or (i == 0 or i == imageHeight - 1):
                put_zeroes(i, j)
                continue
            window = img_arr[i - kernelHeight//2 : i + kernelHeight//2 + 1, j - kernelWidth//2 : j + kernelWidth//2 + 1]
            val = npm.sum(window * kernel)
            vals[i , j] = min(256, max(0, val))
    
    return vals
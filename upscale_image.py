from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


"""
Upscales the given image by a specified factor.

Args:
    input_img (PIL.Image): The input image to be upscaled.
    factor (int): The factor by which to upscale the image.
    lookup (PIL.Image): The lookup image to use for upscaling.

Returns:
    PIL.Image: The upscaled image.
"""
def upscale_image(input_img: Image, factor: int, lookup: Image) -> Image:
    new_x = input_img.size[0] * factor
    new_y = input_img.size[1] * factor
    data = []
    for x in range(new_x // 2):
        for y in range(new_y // 2):
            depth = 0

            try:
                depth = int(lookup.getpixel((x, y)))
            except:
                print(lookup.getpixel((x, y)))
            data.append((depth, depth, depth))
    
    out_img = Image.new('RGB', (new_x, new_y), 'white')
    out_img.putdata(data)
    return out_img



def plot_pixel_density(image: Image):
    # Convert image to grayscale
    # Get pixel values
    pixel_values = np.array(image).flatten()
    
    max = pixel_values.max()
    print("max: ", max)
    for val in pixel_values:
        if val > 100:
            print(val)
    # Plot the density distribution
    plt.figure(figsize=(10, 6))
    plt.hist(pixel_values, bins=256, range=(10, 50), density=True, color='gray', alpha=0.75)
    plt.title('Pixel Value Density Distribution')
    plt.xlabel('Height')
    plt.ylabel('Density')
    plt.show()
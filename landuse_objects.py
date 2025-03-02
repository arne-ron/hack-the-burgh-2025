from PIL import Image
import numpy as npm
def landuse_objects(LiDAR_image, sat_image, red_image):
    class LandUseObject:
        def __init__(self, name, elevation, satColor, redColor, disColor):
            self.name = name
            self.elevation = elevation
            self.satColor = satColor
            self.redColor = redColor
            self.disColor = disColor

    grassland = LandUseObject("Grassland", 63, (70,100,70), (184,80,95), (70,130,70))
    #forest = LandUseObject("Forest", 0, (0,50,0), 0)
    water = LandUseObject("Water", 0, (0,0,30), (0,0,0), (80,80,140))
    urban = LandUseObject("Urban", 160, (95,80,80), (0,0,0), (95,80,80))
    industrial = LandUseObject("Industrial", 255, (220,220,220), (0,0,0), (220,220,220))
    #agriculture = LandUseObject("Agriculture", 0, (255,255,0), 0)
    for obj in [urban, industrial, grassland, water ]:
        newImage = npm.full([*LiDAR_image.shape, 3], 3)
        for i in range(LiDAR_image.shape[0]):
            for j in range(LiDAR_image.shape[1]):
                                                
                elevation_value = LiDAR_image[i][j]
                sat_value = sat_image[i][j]
                red_value = red_image[i][j]

                # Calculate elevation weighting
                elevation_diff = abs(elevation_value - obj.elevation)
                elevation_weighting = max(0, 1 - elevation_diff / 255)

                # Calculate red channel weighting
                redColor_diff = abs(red_value[0] - obj.redColor[0])  # Only compare red channel
                redColor_weighting = max(0, 1 - redColor_diff / 255)

                # Calculate satColor weighting (averaging RGB differences)
                satColor_diff = [abs(int(sat_value[k]) - obj.satColor[k]) for k in range(3)]
                satColor_weighting = npm.mean([1 - d / 255 for d in satColor_diff])

                if obj.name == "Water":
                    weighting = (5/8*elevation_weighting + 1/4*redColor_weighting + 1/2*satColor_weighting) / 3
                elif obj.name == "Grassland":
                    weighting = (1/8*elevation_weighting + 5/8*redColor_weighting + 1/4*satColor_weighting)
                elif obj.name == "Urban":
                    weighting = (1/2*elevation_weighting + 1/4*redColor_weighting + 1/4*satColor_weighting)
                elif obj.name == "Industrial":
                    weighting = (1/2*elevation_weighting + 1/4*redColor_weighting + 1/4*satColor_weighting)
                else:
                    weighting = (elevation_weighting + redColor_weighting + satColor_weighting) / 3
                weighted_color = [int(c * weighting) for c in obj.disColor]
                newImage[i][j] = weighted_color
        Image.fromarray(newImage.astype(npm.uint8), "RGB").show()
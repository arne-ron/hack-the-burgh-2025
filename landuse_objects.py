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

    # grassland = LandUseObject("Grassland", 63, (70,100,70), (184,80,95), (70,130,70))
    # water = LandUseObject("Water", 0, (0,0,30), (0,0,0), (80,80,140))
    # urban = LandUseObject("Urban", 160, (95,80,80), (0,0,0), (95,80,80))
    # industrial = LandUseObject("Industrial", 255, (220,220,220), (0,0,0), (220,220,220))
    grassland = LandUseObject("Grassland", 63, (70,100,70), (184,80,95), (100,0,0))
    water = LandUseObject("Water", 0, (0,0,30), (0,0,0), (100,0,0))
    urban = LandUseObject("Urban", 160, (95,80,80), (0,0,0), (100,0,0))
    industrial = LandUseObject("Industrial", 255, (220,220,220), (0,0,0), (100,0,0))
    classified_images = {}

    for obj in [urban, industrial, grassland, water]:
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
                    weighting = (1/8*elevation_weighting + 1/8*redColor_weighting + 6/8*satColor_weighting)**3
                elif obj.name == "Grassland":
                    weighting = (1/8*elevation_weighting + 5/8*redColor_weighting + 1/4*satColor_weighting)**3
                elif obj.name == "Urban":
                    water_sat_diff = [abs(int(sat_value[k]) - water.satColor[k]) for k in range(3)]
                    water_sat_weighting = npm.mean([1 - d / 255 for d in water_sat_diff])  

                    # Reduce the urban sat weighting by how much it resembles water
                    satColor_weighting = max(0, satColor_weighting - water_sat_weighting)

                    weighting = (1/4 * elevation_weighting + 1/4 * redColor_weighting + 3/2 * satColor_weighting) ** 3
                elif obj.name == "Industrial":
                    weighting = (1/4*elevation_weighting + 0*redColor_weighting + 6/8*satColor_weighting)**3
                else:
                    weighting = (elevation_weighting + redColor_weighting + satColor_weighting)
                weighted_color = [int(c * weighting) for c in obj.disColor]
                newImage[i][j] = weighted_color
        classified_images[obj.name] = newImage
        # Image.fromarray(newImage.astype(npm.uint8), "RGB").show()
    urban_array = Image.fromarray(classified_images["Urban"].astype(npm.uint8), "RGB")
    grassland_array = Image.fromarray(classified_images["Grassland"].astype(npm.uint8), "RGB")
    water_array = Image.fromarray(classified_images["Water"].astype(npm.uint8), "RGB")
    industrial_array = Image.fromarray(classified_images["Industrial"].astype(npm.uint8), "RGB")
    grassland_array = classified_images["Grassland"]
    water_array = classified_images["Water"]
    industrial_array = classified_images["Industrial"]
    urban_array = classified_images["Urban"]


    comparison_image = npm.full_like(urban_array, (0,0,0), dtype=npm.uint8)

    for i in range(LiDAR_image.shape[0]):
        for j in range(LiDAR_image.shape[1]):

            val = comparison_image[i, j]

            if water_array[i,j,0] > 60:
                val = (80, 80, 140)
            if grassland_array[i, j,0] > 65:
                val = (70, 130, 70)
            if urban_array[i,j,0] > 30:
                val = (95, 80, 80)
            if industrial_array[i, j, 0] > 15:
                val = (220, 220, 220)

            comparison_image[i, j] = val
            continue


            #####
            # Deprecated Code
            #####

            # Compute intensity values for each classification
            urban_value = npm.mean(urban_array[i, j])
            grassland_value = npm.mean(grassland_array[i, j])
            water_value = 1/3*npm.mean(water_array[i, j])
            industrial_value = npm.mean(industrial_array[i, j])

            # Determine the strongest classification
            max_value = max(urban_value, grassland_value, water_value, industrial_value)

            if max_value == urban_value:
                comparison_image[i, j] = (95,80,80)
            elif max_value == grassland_value:
                comparison_image[i, j] = (70,130,70)
            elif max_value == water_value:
                comparison_image[i, j] = (80,80,140)
            elif max_value == industrial_value:
                comparison_image[i, j] = (220,220,220)

    # Show the final classified image
    final_res = Image.fromarray(comparison_image, "RGB")
    final_res.save("classification.png")
    final_res.show()

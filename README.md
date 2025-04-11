# hack-the-burgh-2025
This project is our teams submission to the challenge set by Viridien for HackTheBurghXI in Edinburgh 2025 winning the **second place 🥈**.
The goal of the challenge was to upscale a colored satelite photograph of an area near Heathrow using a satelite LiDAR image with 10 times higher resolution in both directions, inheriting as much data from the LiDAR to the colored photograph as possible.
Additionally, the landscape should be analysed in regards to classification and environmental impact.

The running the main.py file performs the calculations on the data given in /data and saves the upscaled image as a `upscaled.tif` in the current folder.
Own images can be used by setting the `input_path_*` variables.

The land use data is created by analysing all 3 datasets, the elevation on a normalised lidar, the degree of redness in the grass satellite image, and the colour values of the satellite image. Then each land type was created as an object and expected values for every pixel in the above datasets assigned to it, then each pixel was weighted to how likely it was to be each land type. Then the probabilities were overlayed and the most likely land use type displayed in the following colours:

### Key

- Blue: Water / Wetlands
- Brown: Urban
- Green: Grass / Woodland
- White: Industry

Note: On a MacBook Pro it takes at least 2-5 minutes to run the file, possibly longer on other devices.

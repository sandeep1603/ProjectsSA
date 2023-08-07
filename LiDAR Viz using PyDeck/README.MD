# LiDAR Point Cloud Visualization with Pydeck

This repository contains Python scripts for processing and visualizing LiDAR point cloud data using the Pydeck library. Pydeck is a powerful library that simplifies the process of creating interactive and visually appealing 3D visualizations, making it an excellent choice for exploring large-scale point cloud datasets.

## Requirements

To run the scripts in this repository, you'll need the following:

- Python 3.x
- Pandas
- Numpy
- laspy
- open3d
- pydeck

You can install the required Python libraries using pip with the following command:

`pip install pandas numpy laspy open3d pydeck`

## Code Description

- Preprocessing.py: This script reads LiDAR point cloud data from a LAS file, converts it to a Pandas DataFrame, and saves it as a CSV file. It also calculates normalized intensity values and adds RGB color information based on intensity for each point. The resulting modified DataFrame is then saved as a new CSV file.

- Lidar_web.py: This script reads the modified CSV file generated from the previous step and downsamples the data to reduce the number of points. It then uses Pydeck PointCloudLayer to create an interactive 3D visualization of the downsampled point cloud. The visualization is saved as an HTML file, which can be opened in a web browser.

## Usage
- Clone the repository to your local machine:
`git clone https://github.com/your-username/lidar-point-cloud-visualization.git`
`cd lidar-point-cloud-visualization`

- Run the data processing script to preprocess the LiDAR point cloud data:

`python Preprocessing.py`

- This will read the LAS file, extract the necessary information, calculate RGB colors based on intensity, and save the modified DataFrame as a CSV file.

- Next, run the visualization script to create an interactive 3D visualization of the downsampled point cloud:

`python Lidar_web.py`

- This script will read the modified CSV file, downsample the data, and create a Pydeck visualization saved as an HTML file.

- Open the generated HTML file point_cloud_visualization_rgb.html in your web browser to explore the 3D visualization of the LiDAR point cloud.

## Customization
- If you want to process a different LAS file, replace the file path in the Preprocessing.py script with your desired LAS file path.

- To adjust the number of points in the visualization, modify the value of n in the sample method within the Lidar_web.py script.

# LiDAR Point Cloud Visualization with Open3D
This repository contains Python scripts for visualizing LiDAR point cloud data using the Open3D library. Open3D is a powerful library that provides tools for processing 3D data and offers visualization capabilities. The provided code allows you to visualize LiDAR point cloud data stored in LAS files and apply grayscale coloring to intensity values.

## Requirements
To run the scripts in this repository, you'll need the following Python libraries:

-numpy: A library for numerical computing in Python.
-laspy: A library for reading and writing LAS files commonly used in LiDAR data processing.
-open3d: A versatile library for 3D data processing and visualization.

-You can install these libraries using pip with the following command:
``` bash 
pip install numpy laspy open3d 
```
## Code Description
The code in this repository provides functionality to read LiDAR point cloud data from a LAS file, visualize it in 3D, and apply grayscale coloring to points based on intensity values.

-The code reads the LAS file using laspy, extracts X, Y, Z coordinates, and intensity values, and stores them in NumPy arrays.
-The script then creates an Open3D point cloud and visualizes it in a 3D window.
-The intensity values are normalized to the range [0, 1] and used to create a grayscale color map.
-The grayscale color map is applied to the point cloud to visualize the intensity distribution.

## Usage
-Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/lidar-point-cloud-visualization.git
```

```bash 
cd lidar-point-cloud-visualization 
```

-Ensure you have the required libraries installed by running:

```bash 
pip install numpy laspy open3d 
```

-Modify the script to specify the path to your LAS file:

`point_cloud = lp.read('path_to_your_las_file.las')`

-Run the Python script:

```bash 
python LiDAR_Viz.py 
```

-The script will display a 3D visualization of the LiDAR point cloud with grayscale colors based on intensity.

# 3D Data Processing and Visualization Repositories

This repository contains three separate Python repositories, each focusing on different aspects of 3D data processing and visualization. Below is a brief overview of each repository and its contents.

## Repository 1: Fisheye Calibration 

This repository contains Python scripts for fisheye camera calibration and undistortion of fisheye images. It utilizes the OpenCV library for camera calibration and undistortion tasks.

### Contents

- **fisheye_calibration.py**: This script performs fisheye camera calibration using OpenCV. It estimates intrinsic camera parameters and distortion coefficients from a set of calibration images with a checkerboard pattern.

- **fisheye_undistortion.py**: This script undistorts fisheye images using the obtained calibration parameters. It displays undistorted images alongside the original ones for comparison.

For usage instructions and further details, refer to the repository's README.md.

## Repository 2: LiDAR Viz using Open3D

This repository contains Python scripts for visualizing LiDAR point cloud data using the Open3D library. It offers tools for processing 3D data and applying grayscale coloring to intensity values.

### Contents

- **LiDAR_Viz.py**: This script reads LiDAR point cloud data from a LAS file, visualizes it in 3D, and applies grayscale coloring based on intensity values.

For usage instructions and further details, refer to the repository's README.md.

## Repository 3: LiDAR Viz using Pydeck

This repository contains Python scripts for processing and visualizing LiDAR point cloud data using the Pydeck library. It simplifies the creation of interactive 3D visualizations, making it suitable for exploring large-scale point cloud datasets.

### Contents

- **Preprocessing.py**: This script reads LiDAR point cloud data from a LAS file, converts it to a Pandas DataFrame, and saves it as a CSV file. It also calculates normalized intensity values and adds RGB color information based on intensity.

- **Lidar_web.py**: This script reads the modified CSV file and creates an interactive 3D visualization using Pydeck's PointCloudLayer.

For usage instructions and further details, refer to the repository's README.md.

Follow the instructions in each repository's README.md to install required libraries and run the provided scripts.

Customize the scripts as needed for your own datasets and requirements.

Feel free to explore each repository for more details about their specific functionalities and usage instructions.

##Authors
- Fisheye Camera Calibration: Sandeep Raj Sagaya Raj
- LiDAR Viz using Open3D: Sandeep Raj Sagaya Raj
- LiDAR Viz using Pydeck: Sandeep Raj Sagaya Raj

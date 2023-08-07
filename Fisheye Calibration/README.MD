# Fisheye Camera Calibration and Image Undistortion

This Python repository contains two scripts that allow you to perform fisheye camera calibration and undistortion on fisheye images. The camera calibration script estimates intrinsic camera parameters and distortion coefficients from a set of calibration images, while the image undistortion script uses the obtained parameters to remove distortion from fisheye images.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- OpenCV: A popular computer vision library for image processing and computer vision tasks.
- NumPy: A library for numerical computing in Python.
- matplotlib: A library for creating visualizations in Python.

You can install these libraries using pip with the following command:

`pip install opencv-python numpy matplotlib`

## Fisheye Camera Calibration

Description

- The fisheye_calibration.py script performs fisheye camera calibration using OpenCV to obtain intrinsic camera parameters, distortion coefficients, and camera matrix for a fisheye camera. The calibration is based on a set of images of a checkerboard pattern.

How to Use

- Place your calibration images in a directory and update the images variable in the script with the path to your image directory. The images should contain a checkerboard pattern with the specified dimensions in the CHECKERBOARD variable (6x9 in this case).

- Run the script:

`python fisheye_calibration.py`

- The script will find the checkerboard corners in the images, perform subpixel refinement, and perform camera calibration to estimate the intrinsic and distortion parameters.

- The script will output the calibration results, including the number of valid images used for calibration (N_OK), the dimensions of the images (DIM), the camera matrix (K), and the distortion coefficients (D).

## Fisheye Image Undistortion

Description

- The fisheye_undistortion.py script performs undistortion on fisheye images using the intrinsic camera parameters and distortion coefficients obtained from fisheye camera calibration. The undistorted images are then displayed side-by-side with the original images for comparison.

How to Use
- Place the fisheye images to be undistorted in a directory and update the image_dir variable in the script with the path to your image directory.

Run the script:

`python fisheye_undistortion.py`

- The script will process each image in the specified directory, perform undistortion, and save the undistorted images in a new directory.

- The undistorted images will be displayed side-by-side with the original images for visual comparison. The undistorted images will have reduced distortion caused by the fisheye lens.

# Import necessary libraries
import numpy as np
import laspy as lp
import open3d as o3d

# Read LAS file using laspy
point_cloud = lp.file.File('1557001110003_1557001110004_Scannerpunkte.las', mode='r')

# Print information about the point cloud
print(point_cloud)  # Print LAS file information
print(len(point_cloud))  # Print the number of points in the point cloud
print(point_cloud.header)  # Print the header information of the LAS file

# Access point cloud attributes
point_cloud.X  # Access the X coordinates
point_cloud.intensity  # Access the intensity values
set(list(point_cloud.classification))  # Get unique classification values
list(point_cloud.point_format.dimensions)  # Get dimensions of point format

# Extract X, Y, Z coordinates and create a NumPy array
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()

# Extract intensity values and create a NumPy array
inten = np.vstack((point_cloud.intensity))

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Visualize the PointCloud
o3d.visualization.draw_geometries([pcd])

# Downsample the PointCloud using voxel downsampling
downsample = pcd.voxel_down_sample(voxel_size=0.5)
print(downsample)

# Normalize the grayscale values to [0, 1]
gray = (inten - inten.min()) / (inten.max() - inten.min())

# Shift the minimum value to 0
gray = gray - gray.min()

# Create a color map from the grayscale values
color_map = o3d.utility.Vector3dVector([[v, v, v] for v in gray])

# Set the point cloud colors to the grayscale color map
downsample.colors = color_map

# Visualize the grayscale point cloud with colors
o3d.visualization.draw_geometries([downsample])

# Create an Open3D visualizer
vis = o3d.visualization.Visualizer()
vis.create_window()

# Add the PointCloud geometry to the visualizer
vis.add_geometry(pcd)

# Customize visual options
vis.get_render_option().point_size = 4
vis.get_render_option().background_color = [1, 1, 1]

# Configure the view
ctr = vis.get_view_control()
ctr.set_lookat(pcd.get_center())

# Run the visualization loop
vis.run()

# Close the visualization window
vis.destroy_window()

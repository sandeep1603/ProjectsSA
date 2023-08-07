# Import necessary libraries
import numpy as np
import laspy as lp
import open3d as o3d
import pandas as pd

# Read the LAS file using laspy
point_cloud = lp.file.File('Path of .las file', mode='r')

# Extract X, Y, Z coordinates and intensity values, and store them in NumPy arrays
points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
inten = np.vstack((point_cloud.intensity))

# Create a Pandas DataFrame to hold the extracted data
data_frame = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z, point_cloud.intensity,
                        point_cloud.classification, point_cloud.synthetic,
                        point_cloud.key_point, point_cloud.withheld, point_cloud.scan_angle_rank,
                        point_cloud.user_data)).transpose()

# Define column names for the DataFrame
column_name = ["X", "Y", "Z", "Intensity", "classification", "synthetic", "key_point", "withheld", "scan_angle_rank", "user_data"]

# Create a new DataFrame 'lidar_df' with the extracted data and corresponding column names
lidar_df = pd.DataFrame(data_frame, columns=column_name)

# Save the DataFrame 'lidar_df' to a CSV file '1557001110003_1557001110004_Scannerpunkte.csv'
lidar_df.to_csv('lastocsv.csv')

# Read the CSV file '1557001110003_1557001110004_Scannerpunkte.csv' into a new DataFrame 'las_file'
las_file = pd.read_csv('lastocsv.csv')

# Drop the 'Unnamed: 0' column, if present, as it might be an artifact from saving the DataFrame to CSV
las_file = las_file.drop(columns=['Unnamed: 0'])

# Extract intensity values and normalize them to the range [0, 1]
intensity = las_file["Intensity"].values
normalized_intensity = (intensity - intensity.min()) / (intensity.max() - intensity.min())

# Calculate individual R, G, B values based on the normalized intensity and store them as new columns in 'las_file'
las_file["R"] = (normalized_intensity * 255).astype(int)
las_file["G"] = (normalized_intensity * 255).astype(int)
las_file["B"] = (normalized_intensity * 255).astype(int)

# Save the modified DataFrame 'las_file' to a new CSV file 'modified_1557001110003_1557001110004_Scannerpunkte.csv', without including the default index column
las_file.to_csv("modified_lastocsv.csv", index=False)

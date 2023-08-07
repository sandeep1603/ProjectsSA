# Import necessary libraries
import pydeck
import pandas as pd
import numpy as np

# Define the file path to the CSV containing the modified LiDAR point cloud data
DATA_URL = "path to csv file"

# Read the CSV file into a Pandas DataFrame 'las_file'
las_file = pd.read_csv(DATA_URL)

# Downsample the DataFrame to reduce the number of points for visualization
downsampled_df = las_file.sample(n=500000)  # Change 'n' to your desired number of points

# Configure Pydeck's PointCloudLayer for visualization
point_cloud_layer = pydeck.Layer(
    "PointCloudLayer",
    data=downsampled_df,
    get_position=["X", "Y", "Z"],  # Use 'X', 'Y', 'Z' columns for the 3D coordinates
    get_color=["R", "G", "B"],     # Use 'R', 'G', 'B' columns for point color (RGB values)
    auto_highlight=True,           # Automatically highlight points on hover
    pickable=True,                 # Enable picking/selecting points
    point_size=0.85,               # Set the size of the points in the visualization
)

# Set the initial view state and view type for the visualization
target = [downsampled_df["X"].mean(), downsampled_df["Y"].mean(), downsampled_df["Z"].mean()]
view_state = pydeck.ViewState(target=target, controller=True, rotation_x=15, rotation_orbit=30, zoom=5.3)
view = pydeck.View(type="OrbitView", controller=True)

# Create the Pydeck Deck, incorporating the point cloud layer and visualization settings
deck = pydeck.Deck(point_cloud_layer, initial_view_state=view_state, views=[view])

# Save the Deck as an HTML file for visualization in a web browser
deck.to_html("pointcloud.html", css_background_color="#add8e6")
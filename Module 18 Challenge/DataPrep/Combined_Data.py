import os
import pandas as pd

# Define the folder and file paths
folder_path = r"D:\ASU_Bootcamp_Anaconda\Module 18 Challenge\Resources"
file_names = ["201801-citibike-tripdata_1.csv", "201802-citibike-tripdata_1.csv", "201803-citibike-tripdata_1.csv"]
combined_file_name = "combined_data.csv"
combined_file_path = os.path.join(folder_path, combined_file_name)

# Read and concatenate the CSV files
data_frames = [pd.read_csv(os.path.join(folder_path, file_name)) for file_name in file_names]
combined_data = pd.concat(data_frames, ignore_index=True)

# Ensure correct headers
combined_data.columns = [
    "tripduration", "starttime", "stoptime", "start station id", "start station name",
    "start station latitude", "start station longitude", "end station id", "end station name",
    "end station latitude", "end station longitude", "bikeid", "usertype", "birth year", "gender"
]

# Save the combined data to a new CSV file
combined_data.to_csv(combined_file_path, index=False)

print(f"Combined file with headers saved to: {combined_file_path}")

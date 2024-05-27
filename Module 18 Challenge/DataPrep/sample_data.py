import os
import pandas as pd

# Define the folder and file paths
folder_path = r"D:\ASU_Bootcamp_Anaconda\Module 18 Challenge\Resources"
combined_file_name = "combined_data.csv"
sample_file_name = "sample_data.csv"
combined_file_path = os.path.join(folder_path, combined_file_name)
sample_file_path = os.path.join(folder_path, sample_file_name)

# Check if the combined CSV file exists
if not os.path.exists(combined_file_path):
    print(f"Combined data file not found at: {combined_file_path}")
else:
    # Load the combined CSV file
    combined_data = pd.read_csv(combined_file_path)

    # Take a sample of the data (e.g., first 10,000 rows)
    sample_data = combined_data.head(10000)

    # Define the correct headers
    headers = [
        "tripduration", "starttime", "stoptime", "start station id", "start station name",
        "start station latitude", "start station longitude", "end station id", "end station name",
        "end station latitude", "end station longitude", "bikeid", "usertype", "birth year", "gender"
    ]

    # Set the headers for the sample data
    sample_data.columns = headers

    # Save the sample data to a new CSV file
    sample_data.to_csv(sample_file_path, index=False)

    print(f"Sample file with headers saved to: {sample_file_path}")

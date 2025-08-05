import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# load Dataset 
# Path to the folder containing all the CSVs
folder_path = "C:\\Users\\DELL\\Desktop\\MTD IDS\\MetaMTD\\python coding\\ML\\CICIoT2023"

# List all CSV files in the folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
# Combine them into one DataFrame
df_list = []
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    
    # Optional: Add a column for the attack type from the filename
    attack_type = os.path.splitext(file)[0]  # filename without .csv
    df["Attack_Type"] = attack_type
    
    df_list.append(df)

    # Concatenate all DataFrames
combined_df = pd.concat(df_list, ignore_index=True)

# Save to a single CSV (optional)
combined_df.to_csv("CICIoT2023_combined.csv", index=False)

print("All files combined. Final shape:", combined_df.shape)



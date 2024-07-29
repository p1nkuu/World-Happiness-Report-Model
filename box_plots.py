import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np

# Load the dataset
file_path = r"C:\Users\lzhu2\OneDrive\Desktop\lab 8 MIT\World-Happiness-Report-Model\WHR2018Chapter2OnlineData.xls"
df_plots = pd.read_excel(file_path, header=0)

# Display the first few rows of the dataset
print(df_plots.head())

folder_name = 'box_plots_figs'

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Loop through all numerical columns and create box plots
for column in df_plots.select_dtypes(include=[np.number]).columns:
    plt.figure(figsize=(8, 6))
    df_plots[column].plot.box()
    
    # Set title and labels
    plt.title(f'Box Plot of {column}')
    plt.ylabel(column)
    
    # Save the plot
    plt.savefig(os.path.join(folder_name, f'box_plot_{column}.png'))  # Save to folder
    
    # Optionally, clear the current figure to avoid overlap in plots
    plt.clf()

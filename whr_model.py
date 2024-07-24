import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns

#getting tha data
directory = "World-Happiness-Report-Model"
filename = "WHR2018Chapter2OnlineData.xls"

# Combining the directory and filename into a full path
file_path = r"C:\Users\lzhu2\OneDrive\Desktop\lab 8 MIT\World-Happiness-Report-Model\WHR2018Chapter2OnlineData.xls"
df = pd.read_excel(file_path, header=0)

print(df.head()) #works
print("This is the shape of the df:", df.shape)

nan_count = np.sum(df.isnull(), axis = 0)
print(nan_count)

print(df.dtypes)
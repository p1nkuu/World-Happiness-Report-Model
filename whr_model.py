import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

#getting tha data
directory = "World-Happiness-Report-Model"
filename = "WHR2018Chapter2OnlineData.xls"

# Combining the directory and filename into a full path
file_path = r"C:\Users\lzhu2\OneDrive\Desktop\lab 8 MIT\World-Happiness-Report-Model\WHR2018Chapter2OnlineData.xls"
df = pd.read_excel(file_path, header=0)

# print(df.head()) #works
# print("This is the shape of the df:", df.shape)

# nan_count = np.sum(df.isnull(), axis = 0)
# print(nan_count)

# print(df.dtypes)

#Since we have a string type for the country column, let us try One Hot Encoding
to_encode = list(df.select_dtypes(include = ['object']).columns)
print("Object Data Types to Encode: ", to_encode)

#inspect posible number of values each column may have
print(df[to_encode].nunique())
top_70_C = list(df['country'].value_counts().head(70).index)
print(top_70_C)
#print(list(df['country'].value_counts()))
# to_encode_values = list(df['country'])


for value in top_70_C:
    
    ## Create columns and their values
    df['OneHot_'+ value] = np.where(df['country']==value,1,0)
    
    
# Remove the original column from your DataFrame df
df.drop(columns = 'country', inplace=True)

#print(df.head())
#print(df.loc[97]['OneHot_Bangladesh']) #to check if alue is on
#print(df.columns)


# we arent using pandas for this since there are too many values are we are just selecting the top 70 
#if there were smaller datas with less features for one hot, we can just use the get_dummies and then concatenete 

#detecting and replacing outliers 
#go through all the data and if there are too many nulls, we can drop the columns all togehter else we can winsorize 

df_summ = df.describe()
print(df_summ)
column_ranges = df_summ.loc['max'] -  df_summ.loc['min']
column_range_name = column_ranges.idxmax()
# print('Col with largest range, ', column_range_name) #healthy life expectancy at birth

df.plot.box()

plt.title('Box Plot of DataFrame')
plt.show()

# print(df.dtypes)

# for column in df.columns:
#     df[]

# need to add the feature list
feature_list = ['year', 'Life Ladder', 'Log GDP per capita', 'Social support', 'Freedom to make life choices', 'Generosity', 
                'Perceptions of corruption', 'Positive affect', 'Negative affect', 'Confidence in national government', 
                'Democratic Quality', 'Delivery Quality', 'GINI index (World Bank estimate), average 2000-15']
df.drop

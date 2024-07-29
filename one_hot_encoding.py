import pandas as pd
import numpy as np
import os 
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

from whr_model import df

to_encode = list(df.select_dtypes(include = ['object']).columns)
#print("Object Data Types to Encode: ", to_encode)

#inspect posible number of values each column may have
#print(df[to_encode].nunique())
top_70_C = list(df['country'].value_counts().head(70).index)
#print(top_70_C)
#print(list(df['country'].value_counts()))
# to_encode_values = list(df['country'])


for value in top_70_C:
    
    ## Create columns and their values
    df['OneHot_'+ value] = np.where(df['country']==value,1,0)
    
    
# Remove the original column from your DataFrame df
df.drop(columns = 'country', inplace=True)


#print(df.head())
#print(df.loc[97]['OneHot_Bangladesh']) #to check if alue is on
print(df.columns)
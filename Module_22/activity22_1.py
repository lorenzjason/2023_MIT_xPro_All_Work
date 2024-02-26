import pandas as pd
from dask import dataframe as dd

#create pandas dataframe
pandas_df = pd.DataFrame({'odd_num':[1,3,5,7,9], 'even_num':[2,4,6,8,10]})

#set npartition argument
df = dd.from_pandas(pandas_df, npartitions = 2)

#Uncomment the line below if you are using Mac
df.to_csv("/Users/jasonl/Documents/Data_E/Module_22/activity22.1/", index=False)

#Uncomment the line below if you are using Windows
#df.to_csv("C:/tmp/mo-pcde/activity22.1/", index=False)
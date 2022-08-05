import pandas as pd


# Reading the file
df=pd.read_excel("file_name.xlsx")
# Checking
print(df)

#df['product'] # to select only one column
selected=df[['col1','col2','col3']]# to select multiple columns
print(selected)
# Making the pivot table
pivot_table = selected.pivot_table(index='col1', columns='col2', values='col3',aggfunc='sum').round(0)
print(pivot_table)

pivot_table.to_excel('pivot_table.xlsx',"Report", startrow=4)





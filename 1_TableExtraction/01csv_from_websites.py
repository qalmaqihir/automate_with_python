import pandas as pd
#this project is kind of webscrapping

# Reading a .csv froma URL with  pandas
# Paste the link of the csv file from the website... (path to the csv file, either local machine or on a website)
df_csv_file=pd.read_csv("")

# Checking the dataframe
print(df_csv_file)

# If you need to rename the columns names
df_csv_file.rename(columns={"old_col1":"new_name",
                            "old_col2":"new_name2"}, inplace=True)

print(df_csv_file)







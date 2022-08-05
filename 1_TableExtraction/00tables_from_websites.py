import pandas as pd


#Paste a link and it will return all the tables on the website
tables = pd.read_html("")

#Lets see how many tables are there
print(len(tables))

#Which ever table we need, chose from the list, lets say we need the first one

print(tables[0])
print(tables[1])
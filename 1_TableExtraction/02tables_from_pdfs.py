"""
also install its two dependencies
pip install tk
pip install ghostscript
------------------------------------------
First install the library camelot-py
pip install camelot-py
"""
import camelot

# Provide the page number, and use either lattice or stream for parsing as flavor
tables = camelot.read_pdf("file_name.pdf",page="1")
# Check the tables type and what is inside => it will have TableList and n=num_of_tables in the page
print(tables)

# Export the table you need to csv
# If you have one table on the page
tables.export("name.csv",f='csv',compress=True)

## if you have more then one table then use the code below, table[0], table[1,2...] loop for getting all the tables
#tables[0].to_csv('name.csv')


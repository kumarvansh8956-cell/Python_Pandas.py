import pandas as p

ds = p.read_csv('Pandas.py/car details v4.csv')
print(ds)
ds.info()


'''

info() method is used to display a concise
 summary of a Pandas DataFrame, including the number of rows, 
 columns, non-null values, data types, and memory usage.
 
 '''
print("  this static summary ")

print(ds.describe())
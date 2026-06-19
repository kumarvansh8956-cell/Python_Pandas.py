import pandas as p

print("_____ Here the dataset _____")
ds = p.read_csv("Outout2.csv")
print(ds)

# Accessing  any specific column
print(' here "Name" column')
print(ds['Name'])

# Accessing multiple column

print(ds[["Name","Degree","City"]])
print( ds.columns)

print()
# filtering
print()
# for single column with single condition

print(ds[ds[' CGPS'] > 8.])
print()
print(ds[ds[' CGPS'] < 8.])
# for culumn with more then one condition

print( "AND logic")
print(ds[(ds[' CGPS'] > 8.)&(ds['Degree'] == "AI&ML")])
print(" OR logic")
print(ds[(ds[' CGPS'] > 8.)|(ds['Degree'] == "AI&ML")])
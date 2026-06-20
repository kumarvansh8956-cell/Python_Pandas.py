import pandas as p

ds = p.read_csv("Outout2.csv")
print(" cuurent dataset")

print(ds)

print(" Adding a columns")

# direct method

ds['intership'] = [1,2,3,4,5] 

ds['CGPS * 10'] = ds[" CGPS"] * 10

print(ds)

# At any specific position
'''
syntax = 

ds.insert(loc,"new_column_name", data)

'''
ds.insert(3,"Company", ['abc','dfg','sdf','ert','yhn'])

print(ds)

# Updating vale in soecific cell

'''
ds.loc[Row_index,"Column_name"]= new value

'''

ds.loc[1," CGPS"] = 6.2

print(ds)

ds.to_csv("New.csv", index= False)
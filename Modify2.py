import pandas as p

ds = p.read_csv('New.csv')

print(ds)

# updating whole column

ds[' CGPS'] = ds[' CGPS'] /5
print(ds)

# removing a column
'''
ds.drop(column = [column1,column2,---], inplace = True)
 inplace = True : it modify orignal dataframe
 inplace = False : it modify and return a copy dataframe

'''
df = ds.drop(columns= ['CGPS * 10',' CGPS'], inplace= False)
print(df)
ds.drop( columns= ['intership'], inplace= True)
print(ds)
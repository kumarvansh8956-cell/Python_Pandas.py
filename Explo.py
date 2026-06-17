import pandas as p


ds = p.read_csv("Pandas.py/car details v4.csv")

print(ds.head())

print(ds.head(10))
print(ds.tail(10))
print(ds.tail())
'''
.head(n) this methods use to see the starting n raws
.tail(n) this methods use to see the last n raws

default value of n is  5

'''
print(ds.shape)

print(ds.columns)

print(ds.dtypes)
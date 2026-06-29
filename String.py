import pandas as p 

df = p.read_csv("Pandas.py/car details v4.csv")

print(df)


print(df.columns)
df['Engine'] = df['Engine'].str.replace("cc","")
df['Max Power'] = df['Max Power'].str.extract(r"(\d+)")

''' 
this is similar to python string functions

'''
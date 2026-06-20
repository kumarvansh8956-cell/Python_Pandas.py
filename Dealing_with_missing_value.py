import pandas as p
'''
Pandas has mainly two type of missing value
 -NaN = not a number
 -None = it for object data type

'''
data = p.DataFrame({
  'Name':['abc','ert', None,'wer', None,'fvg','kai','jai','rai'],
  'Age': [22, None,24,32,65,20, None,23,27],
  'Salary': [None,30000,34000,113400,None,65000,None,50000,3700],
  'Performance_score': [54,90, None,65,34,None,77,84,34],
  'emp_ID': [101,102,103,104,105,106,107,108,109]
})
print(data)

'''
detecting the missing data
use .isnull
syntax:-
  data.isnull()


True - Value is missing
False - Value is present

'''
print(' the missing data is---')
print(data.isnull())

'''
for detect the total number of missing value use
 Sytax
 data.isnull().sum()

'''
a = data.isnull().sum()
print(f" the total number of the missing data is \n {a}")

'''
.dropna()
 this method use to remove entire raws or column

 syntax:-

 data.dropna( axis , inplce = True)
axis=1; it means remove all  columns with missing value
axis=0; it means remove all  rows with missing value , it default
inplace = True; means change in original
inplace = False; means change in copy 
'''
print("columns without missing data")
da  = data.dropna(axis= 1 , inplace= False)
print(da)
print()
print("rows with missing value")
data.dropna(axis= 0 , inplace= True)
print(data)

'''
.fillna()
this method is use to replace the missing value
syntax:-
data.fillna(value , inplace = true)

'''
print(" replacing ")
data.fillna(00 , inplace = True)
print(data)
import pandas as p
data = p.DataFrame({
  'Name':['abc','ert', 'fdr',None, None,'fvg','kai','jai','rai'],
  'Age': [22, None,24,32,65,20, None,23,27],
  'Salary': [None,30000,34000,113400,None,65000,None,50000,3700],
  'Performance_score': [54,90, None,65,34,None,77,84,34],
  'emp_ID': [101,102,103,104,105,106,107,108,109]
})
print(data)

'''
.fillna()
this method is use to replace the missing value
syntax:-
data.fillna(value , inplace = true)

'''
print(" replacing ")
data["Name"] = data['Name'].fillna("N/a")
int_data = ['Age',   'Salary',  'Performance_score']
data[int_data]= data[int_data].fillna( 00 , inplace = True)

print(data)

'''
.interpolate()

This method is used to fill missing values (NaN)
by estimating values from nearby data points.

Syntax:
data.interpolate(method='linear', inplace=True)

Parameters:
method  -> technique used to estimate missing values
inplace -> True = modify original DataFrame
           False = return new DataFrame

Common Methods:

1. linear (default)
   Fills NaN using a straight-line relationship
   between previous and next values.

2. nearest
   Replaces NaN with the nearest available value.

3. ffill (Forward Fill)
   Copies the previous valid value forward.

   Syntax:
   data.ffill()

4. bfill (Backward Fill)
   Copies the next valid value backward.

   Syntax:
   data.bfill()

5. polynomial
   Uses polynomial curve fitting to estimate values.

   Syntax:
   data.interpolate(method='polynomial', order=n)

6. spline
   Uses spline curve fitting for smoother estimation.

   Syntax:
   data.interpolate(method='spline', order=n)
 here "order" representing the degree  
 order = 1 is linear line
 order = 2 is quadratic curve , and so more
Example:

Before:
10
NaN
30

After Linear Interpolation:
10
20
30

Note:
Interpolation works only on numerical data.
It is not suitable for string or categorical columns.
'''
da = {
  'Name':['abc','ert', 'fdr','eecc', 'ertde','fvg','kai','jai','rai'],
  'Age': [22, None,24,32,65,20, None,23,27],
  'Salary': [None,30000,34000,113400,None,65000,None,50000,3700],
  'Performance_score': [54,90, None,65,34,None,77,84,34],
  'emp_ID': [101,102,None,104,None,106,107,108,109]
}
data2 = p.DataFrame(da)
print(data2)
data2['Salary'] = data2['Salary'].bfill()

data2['Age'] = data2['Age'].interpolate(method='nearest')
data2['emp_ID'] = data2['emp_ID'].interpolate(method='polynomial', order= 2)
data2['Performance_score'] = data2['Performance_score'].interpolate(method='spline', order= 2)
print(data2)
# Quick summary
'''

.interpolate()

Used to fill missing numerical values by estimating
them from surrounding data.

Syntax:
data.interpolate(method='linear', inplace=True)

Methods:
linear   -> straight-line estimation (default)
nearest  -> nearest valid value
ffill    -> copy previous value
bfill    -> copy next value
polynomial -> polynomial curve fitting
spline     -> spline curve fitting

Works best for numerical data.
'''

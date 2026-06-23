import pandas as p
'''

data.groupby('column1')[column2].opertion

this method group up the data on based on column1 and applied opertion on column2 values
example 
column1 a,a,s,f,a,f,f,d,s,o,a 
column2 11,33,2,4,54,5,20,54,22
then groupby
a  [11,33,4,22]
s [ 2,20]
f [2,54,5]
o [54]
data.groupby('column1')[column2].count()
output :-
a  3
s 2
f 3
o 1


'''
data = p.read_csv("Pandas.py/car details v4.csv")

print("Data_Set")
print(data)
Group = data.groupby("Make")['Price'].count()
print(Group)
print(Group.max())
Group2 = data.groupby("Make")['Price'].mean()
print(Group2)

'''
its take list two
data.groupby(['column_list1'])[column_list2].opertion

'''
print('here')
Group3 = data.groupby(["Make",'Model'])['Price'].count()
print(Group3)
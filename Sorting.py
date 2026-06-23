import pandas as p

data =  {
  "Name":['Vansh','Mann','Dheeraj','Prithvi','Arman'],
  "D_O_B": [2006,2007,2005,2005,2005],
  "Field": ['AI','Graphic_designing','Data_Science','Cybersecurity','Data_analysis'],
  "City": ['Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad'],
  "Degree":["AI&ML","CA,","AI&ML","CSE","AI&ML"],
  " CGPS":[9, 7.9,8,8.3,9.1]
}
Data_frame = p.DataFrame(data)
print(Data_frame)

'''
Sort an any specific column

Data_Frame.sort_values(by="column_name",ascending = True/False, inplace= True/False)
 False = Descending order = increasing order
True = ascending order = decreasing order


'''

print("sorting")
Data_frame.sort_values(by=" CGPS",ascending =  True , inplace= True)
print(Data_frame)

'''
Sort an any Multiple columns

Data_Frame.sort_values(by=["List_of_column_name],ascending = [List True/False] , inplace= True/False)
 False = Descending order = increasing order
True = ascending order = decreasing order


'''
print(" sorting more than one column")
Data_frame.sort_values(by=["Name",'D_O_B',"Degree"],ascending = [True,False,True] , inplace= True)
print(Data_frame)
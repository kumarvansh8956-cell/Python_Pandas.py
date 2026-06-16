import pandas as p
''' creating a dataframe'''
data =  {
  "Name":['Vansh','Mann','Dheeraj','Prithvi','Arman'],
  "D_O_B": [2006,2007,2005,2005,2005],
  "Field": ['AI','Graphic_designing','Data_Science','Cybersecurity','Data_analysis'],
  "City": ['Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad'],
  "Degree":["AI&ML","CA,","AI&ML","CSE","AI&ML"]
}
Data_frame = p.DataFrame(data)
print(Data_frame)

# saving the dataframe in formate of file
Data_frame.to_csv("Outout.csv")
Data_frame.to_excel("Output.xlsx")
Data_frame.to_json('Output.json')
Data_frame.to_csv("Outout2.csv",index=False)
 
'''
 syntax:=

 Dataframe.to_Formate('name for new file')

 without index

 
 Dataframe.to_Formate('name for new file', index = false)

 
 '''

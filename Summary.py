import pandas as  p
data =  {
  "Name":['Vansh','Mann','Dheeraj','Prithvi','Arman'],
  "D_O_B": [2006,2007,2005,2005,2005],
  "Field": ['AI','Graphic_designing','Data_Science','Cybersecurity','Data_analysis'],
  "City": ['Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad','Ghaziabad'],
  "Degree":["AI&ML","CA,","AI&ML","CSE","AI&ML"],
  "CGPS":[9, 7.9,8,8.3,9.1]
}
Data_frame = p.DataFrame(data)
print(Data_frame)

Avg_CGPS = Data_frame["CGPS"].mean()
print(Avg_CGPS)

print(Data_frame['D_O_B'].std())
print(Data_frame["CGPS"].min())
print(Data_frame["CGPS"].max())
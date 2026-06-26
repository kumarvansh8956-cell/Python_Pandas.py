import pandas as pd

# ---------------- Student Dataset ----------------
students = {
    "Student_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Neha", "Karan"],
    "Age": [20, 21, 20, 22, 21],
    "Gender": ["M", "F", "M", "F", "M"],
    "Branch": ["CSE", "AI", "ECE", "CSE", "ME"],
    "Semester": [4, 6, 4, 8, 6],
    "CGPA": [8.5, 9.1, 7.8, 8.9, 7.5],
    "City": ["Delhi", "Mumbai", "Jaipur", "Pune", "Lucknow"],
    "Club": ["AI", "Robotics", "Coding", "Dance", "Sports"],
    "Attendance": [92, 95, 88, 90, 85]
}

df1 = pd.DataFrame(students)

# ---------------- Result Dataset ----------------
results = {
    "Student_ID": [101, 102, 103, 105, 106],
    "Subject": ["Python", "ML", "DBMS", "CAD", "AI"],
    "Marks": [89, 95, 76, 82, 91],
    "Grade": ["A", "A+", "B", "A", "A+"],
    "Faculty": ["Sharma", "Gupta", "Singh", "Verma", "Mehta"],
    "Exam_Type": ["Mid", "Final", "Mid", "Final", "Mid"],
    "Project": ["Yes", "Yes", "No", "Yes", "Yes"],
    "Internship": ["Yes", "Yes", "No", "No", "Yes"],
    "Scholarship": ["No", "Yes", "No", "No", "Yes"],
    "Placement": ["No", "Yes", "No", "Yes", "No"]
}

df2 = pd.DataFrame(results)

# Display datasets
print("Students Dataset")
print(df1)

print("\nResults Dataset")
print(df2)

# concat() Method

"""
Syntax:
pd.concat([list of data-sets], axis=0)

Purpose:
- Combines two or more DataFrames.
- No common key is required.

Parameters:

1. axis=0 (Default)
   - Stacks DataFrames vertically (row-wise).

2. axis=1
   - Combines DataFrames horizontally (column-wise).

3. ignore_index=True
   - Resets the index after concatenation.

Notes:
- Missing values are filled with NaN.
- Does not match rows using a key.
- Can concatenate multiple DataFrames at once.


"""
print('Vertical')
print( pd.concat([df1, df2], axis=0))
print('horizontal')
h_c= pd.concat([df1, df2], axis=1)
print('\n', h_c)
print(h_c.columns)
print("reset the index")
print('\n',pd.concat([df1, df2], ignore_index=True))
print('do not reset the index ')
print('\n',pd.concat([df1, df2], ignore_index=False))
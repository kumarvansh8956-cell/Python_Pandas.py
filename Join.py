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

# join() Method

"""
Syntax:
df1.join(df2, how="type_of_join")

Purpose:
- Combines two DataFrames using their INDEX.
- If needed, a column can be converted to an index using set_index().

Types of Join:

1. inner
   - Returns only the common indexes.

2. left (Default)
   - Returns all indexes from the left DataFrame.
   - Missing values from the right DataFrame are filled with NaN.

3. right
   - Returns all indexes from the right DataFrame.
   - Missing values from the left DataFrame are filled with NaN.

4. outer
   - Returns all indexes from both DataFrames.
   - Missing values are filled with NaN.

Notes:
- Uses INDEX instead of a common column.
- Faster and simpler than merge() when joining by index.


"""
df1 = df1.set_index("Student_ID")
df2 = df2.set_index("Student_ID")
print(" join by inner")
join_in =  df1.join(df2, how="inner")
print(join_in)
print(" join by outer")
join_out =  df1.join(df2, how="outer")
print(join_out)
print(" join by the default or left")

join_left =  df1.join(df2)
print(join_left)

print(" join by the right")
join_right =  df1.join(df2, how="right")
print(join_right)
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

# merge_method
# merge() method

"""
Syntax:

pd.merge(data_set_1, data_set_2, on="key", how="type_of_merge")

Here:
key -> Common column present in both datasets.
       It acts as a bridge (joining key) between the datasets.

Types of Merge

1. inner
   - Returns only the rows where the key exists in both datasets.

2. outer
   - Returns all rows from both datasets.
   - Missing values are filled with NaN.

3. left
   - Returns all rows from the left dataset.
   - If a matching key is not found in the right dataset,
     the right-side columns contain NaN.

4. right
   - Returns all rows from the right dataset.
   - If a matching key is not found in the left dataset,
     the left-side columns contain NaN.

5. cross
   - Returns the Cartesian Product.
   - Every row of dataset1 is paired with every row of dataset2.
   - it does not take 'on'
   syntax = pd.merge(df1, df2, how="cross")
   If dataset1 has shape (a x b)
   and dataset2 has shape (p x q)

   Output rows = a x p

"""
print('Inner Merge ')
in_merge = pd.merge(df1, df2, on="Student_ID", how="inner")
print(in_merge)

print('Outer Merge ')
out_merge = pd.merge(df1, df2, on="Student_ID", how="outer")
print(out_merge)

print(' left Merge ')
left_merge = pd.merge(df1, df2, on="Student_ID", how="left")
print(left_merge)
print('Right Merge ')
right_merge = pd.merge(df1, df2, on="Student_ID", how="right")
print(right_merge)
print('Cross Merge ')
Cross_merge = pd.merge(df1, df2, how="cross")
print(Cross_merge)
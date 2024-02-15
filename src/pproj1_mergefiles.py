'''
PROJECT DETAILS : 
A MINI PROJECT USING PANDAS TO COMBINE 2 FILES AND SHARE OUTPUT OF THE 
SELECTED COLUMN IN A SINGLE FILE OT TABLE FORMAT
Data Source : https://www.kaggle.com/datasets/dillonmyrick/high-school-student-performance-and-demographics?resource=download
High School Student Performance & Demographics
High school student perfomance as well as demographic, social, and parent data.

File Names : student_portuguese_clean.csv and student_math_clean

'''

import pandas as pd

#Read data from File stored in 'Google Drive / data' directory
df = pd.read_csv("data/student_math_clean.csv")
df1 = pd.read_csv("data/student_portuguese_clean.csv")
#select only required columns
selected_col = ["student_id","school","sex","age","address_type","final_grade"]
# display only selected columns
df_selected_columns = df[selected_col]
df_selected_columns1 = df1[selected_col]
#show the selected column where 'student_id' is same
df_merge = pd.merge(df_selected_columns,df_selected_columns1, on="student_id", how="left")
# print Merged data.
print(df_merge)
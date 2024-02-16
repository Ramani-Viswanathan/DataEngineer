'''
PROJECT DETAILS : 
PySpark February 2024 Batch – Assignment 1

Project work on pandas:
Id	Batch start date	Batch end date	Email	Name	Employee id

Create data directory and create 3 excel files with the above format
Put some dummy data in each file
Write pandas code (.py) to read each excel files and combine the data from these 3 input file.
Select only ID, email, Name and generate an output excel file with the combined data


'''
# import panda library
import pandas as pd

# Read data from File stored in ' data' directory, assigned to Data Frame df1, df2,df3
df1 = pd.read_excel("data/training_batch_1.xlsx")
df2 = pd.read_excel("data/training_batch_2.xlsx")
df3 = pd.read_excel("data/training_batch_3.xlsx")

#select only required columns
selected_col = ["id","email","name"]

# add the selected column in data frame
df_selected_columns1 = df1[selected_col]
df_selected_columns2 = df2[selected_col]
df_selected_columns3 = df3[selected_col]

#Append all 3 daata frame into 1 data frame
df_append = pd.concat([df_selected_columns1, df_selected_columns2, df_selected_columns3],ignore_index=True)

#write to excel file, create a file in google drive
df_append.to_excel("data/training_batch_consolidated.xlsx",sheet_name='Consolidated')

#print the appended output for validation
print (df_append)
import pandas as pd
import streamlit as st
import openpyxl as px
import markdown as md

header = st.container()
dataset = st.container()

with header:
    st.title("Infor LN New Users")
    st.image("userInvite.png")
    st.divider()

file_path = "NewUsers_2025.xlsx"
#column_name = st.text_input("Enter the training name")

column_name = pd.read_excel('trainingName.xlsx')

role = st.selectbox('Select a role', column_name, index = None,
    placeholder="Select training name",)

def find_last_empty_row(file_path, column_name):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Check if the column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the dataframe.")
    
    # Get the column data
    column_data = df[column_name]
    
    # Find the first empty row in the column
    first_empty_row = column_data[column_data.isna()].index[0]
    
    return first_empty_row

#Validation of first empty row in a specific Column
try:
    last_empty_row = find_last_empty_row(file_path, column_name)
    print(f"The first empty row in column '{column_name}' is: {last_empty_row}")
except ValueError as e:
    print(e)
except IndexError:
    print(f"No empty rows found in column '{column_name}'")

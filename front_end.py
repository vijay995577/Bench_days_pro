import pandas as pd
import streamlit as st
from PIL import Image
import datetime as dt
im = Image.open('thundersoft.png')
excel_data = pd.read_excel("demo1.xlsx")
name = list(excel_data.EmployeeName)
#print(name)

def Emp_detils(emp_inp,search_by):
    excel_data = pd.read_excel("demo1.xlsx")
    data = excel_data.loc[excel_data[search_by]==emp_inp]
    cols =(list(data))
    on_board_date = list(data['Project1 Onboard'])
    off_board_date = list(data['Project1 Offboarding'])
    print((on_board_date))
    print(off_board_date)



col1,col2,col3 = st.columns([5,5,5])

with col1 :
    st.image(im)

search_by =st.selectbox('Search By',('EmployeeName',"EmployeeID"))
emp_inp = st.text_input("Enter Employee details")
if st.button('Submit'):
    Emp_detils(emp_inp,search_by)
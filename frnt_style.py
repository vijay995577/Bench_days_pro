import pandas as pd
import streamlit as st
from PIL import Image
import datetime as dt

# st.set_page_config(layout="wide")
im = Image.open('thundersoft.png')

excel_data = pd.read_excel("demo2.xlsx")
name = list(excel_data["EmployeeName"])
# name = name.insert(0,"Select Employee Name")
ids = list(excel_data['EmployeeID'])


def details(emp_inp, search_by):
    emp_det = excel_data.loc[excel_data[search_by] == emp_inp]
    # st.write(emp_det)
    index_of_row = list(emp_det.index)[0]
    print(index_of_row)

    on_board_date_proj1 = list(emp_det['Project1 Onboard'])
    on_board_date_proj2 = list(emp_det['Project2 Onboard'])
    off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
    off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
    join_date = list(emp_det['Joining Date'])

    bench_days = 0
    proj1_days = 0
    proj2_days = 0

    if on_board_date_proj1[0] == "None":
        bench_days = (dt.datetime.now() - join_date[0]).days
        print('1st if')
    elif (off_board_date_proj1[0]) == 'None' and (on_board_date_proj1[0]) != "None":
        print('2nd if')
        # print(type(on_board_date_proj1[0]))
        bench_days += (on_board_date_proj1[0] - join_date[0]).days
    elif (off_board_date_proj1[0]) != "None" and (on_board_date_proj2[0]) == 'None':
        print('3RD IF')
        proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
        bench_days += (dt.datetime.now() - off_board_date_proj1[0]).days
        bench_days += (on_board_date_proj1[0] - join_date[0]).days()
        # print(bench_days)
    elif on_board_date_proj2[0] != "None" and off_board_date_proj2[0] == 'None':
        print('4th if')
        proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
        bench_days += (on_board_date_proj2[0] - off_board_date_proj1[0]).days
        bench_days += (on_board_date_proj1[0] - join_date[0]).days
    elif off_board_date_proj2[0] != 'None':
        print('5th if')
        # bench_days += dt.datetime.now() - off_board_date_proj2[0]
        bench_days += (on_board_date_proj2[0] - off_board_date_proj1[0]).days
        bench_days += (on_board_date_proj1[0] - join_date[0]).days
        bench_days += (dt.datetime.now() - off_board_date_proj2[0]).days
        proj2_days = (off_board_date_proj2[0] - on_board_date_proj2[0]).days
        proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
    else:
        print('else')
        pass

    # st.write('Project1 days:', proj1_days)
    # st.write('Project2 days:', proj2_days)
    # st.write(' Bench Days :', bench_days)
    def bench_days_update():
        pass

    excel_data.at[index_of_row, 'Bench Days'] = int(bench_days)
    # print(excel_data.tail(5))
    excel_data.to_excel("demo2.xlsx", index=False)
    emp_det = excel_data.loc[excel_data[search_by] == emp_inp]
    st.write(emp_det)

    for i in emp_det:
        if i == 'Bench Days':
            st.write(i, ":", bench_days)
            st.write('Project1 days:', proj1_days)
            st.write('Project2 days:', proj2_days)
            break
        else:
            st.write(i, ":", list(emp_det[i])[0])


col1, col2, col3 = st.columns([5, 5, 5])
with col1:
    st.image(im)

search_by = st.selectbox('Search By', ('EmployeeName', "EmployeeID"))
if search_by == 'EmployeeName':
    emp_inp = st.selectbox("Enter Employee details", name)
    if st.button('Submit'):
        if (emp_inp not in name):
            st.error('Please give proper input')
        else:
            details(emp_inp, search_by)

else:
    emp_inp = st.selectbox("Enter Employee details", ids)
    if st.button('Submit'):
        if (emp_inp not in ids):
            st.error('Please give proper input')
        else:
            details(emp_inp, search_by)







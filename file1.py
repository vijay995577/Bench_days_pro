import pandas as pd
import streamlit as st
from PIL import Image
import datetime as dt
from dataupdate import Update
icon = Image.open('tslogo.jpg')

#streamlit page configration
st.set_page_config(
    page_icon=icon,
    page_title='Employee Details',
    layout= "wide"
)




#st.set_page_config(layout="wide")
im = Image.open('thundersoft.png')


excel_data = pd.read_excel("demo2.xlsx")
name = list(excel_data["EmployeeName"])
ids= list(excel_data['EmployeeID'])
obj= Update()


def details(emp_inp,search_by):
        emp_det = excel_data.loc[excel_data[search_by] == emp_inp]
        on_board_date_proj1 = list(emp_det['Project1 Onboard'])
        on_board_date_proj2 = list(emp_det['Project2 Onboard'])
        on_board_date_proj3= list(emp_det['Project3 Onboard'])
        off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
        off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
        off_board_date_proj3 = list(emp_det['Project3 Offboarding'])
        join_date = list(emp_det['Joining Date'])

        bench_days = 0
        proj1_days = 0
        proj2_days = 0
        proj3_days = 0
        status="Bench"
        try :
            if (join_date[0]) == 'None':
                print('0 if ')
                st.error('Candidate was not Onboarded till now')

            elif (on_board_date_proj1[0]) == "None":
                print('1st if')
                bench_days += (dt.datetime.now() - join_date[0]).days

            elif (off_board_date_proj1[0]) == 'None' and (on_board_date_proj1[0]) != "None":
                print('2nd if')
                status = "Project 1"
                proj1_days = (dt.datetime.now() - on_board_date_proj1[0]).days

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
                status = "Project 2"
                proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
                proj2_days= (dt.datetime.now() - on_board_date_proj2[0])
                bench_days += (on_board_date_proj2[0] - off_board_date_proj1[0]).days
                bench_days += (on_board_date_proj1[0] - join_date[0]).days
            elif off_board_date_proj2[0] != 'None' and on_board_date_proj3[0] == 'None' :
                print('5th if')
                # bench_days += dt.datetime.now() - off_board_date_proj2[0]
                bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
                bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                bench_days += (dt.datetime.now().date() - off_board_date_proj2[0].date()).days
                proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
                proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
            elif on_board_date_proj3[0] != 'None' and off_board_date_proj3[0] == "None":
                print('6th if')
                bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
                bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                bench_days += (on_board_date_proj3[0].date() - off_board_date_proj2[0].date()).days
                proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
                proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
                proj3_days = (dt.datetime.now().date() - on_board_date_proj3[0].date()).days
            elif off_board_date_proj3[0] != "None":
                print('7th if')
                bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
                bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                bench_days += (on_board_date_proj3[0].date() - off_board_date_proj2[0].date()).days
                bench_days += (dt.datetime.now().date() - off_board_date_proj3[0].date()).days
                proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
                proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
                proj3_days = (off_board_date_proj3[0].date() - on_board_date_proj3[0].date()).days
            else:
                print('else')
                pass
        except Exception:
            print(Exception)
            print('An erroe occured in if else block')
        st.write(emp_det)
        
        lis= ['EmployeeName','EmployeeID' ] #,'Bench Days','Status']
        for i in emp_det:
            if i=='Bench Days':
                st.write((i),":",int(bench_days))
                st.write('Project1 days:' ,proj1_days)
                st.write('Project2 days:' ,proj2_days)
                st.write("Project3 days",proj3_days)
                st.write('Status:',status)
                break
            else:
                try:
                    if i in lis:
                        st.write(i,':',list(emp_det[i])[0])
                except NameError:
                    print(NameError,'Name not in lis')
col1,col2,col3 = st.columns([5,5,5])
with col1 :
    st.image(im)

search_by =st.selectbox('Search By',('EmployeeName',"EmployeeID"))
if search_by == 'EmployeeName':
    emp_inp = st.selectbox("Enter Employee details",name)
    if st.button('Submit'):
        if (emp_inp not in name):
            st.error('Please give proper input')
        else:
            details(emp_inp,search_by)
    if st.button("Update All"):
        try:
            obj.all_col()
            st.success('you updated all bench days')
        except:
            print('except')

else:
    emp_inp = st.selectbox("Enter Employee details",ids)
    if st.button('Submit'):
        if (emp_inp not in ids):
            st.error('Please give proper input')
        else:
            details(emp_inp,search_by)
        if st.button("Update All"):
            try:
                obj.all_col()
                st.success('you updated all bench days')
            except:
                print('Except in Bench days class calling')







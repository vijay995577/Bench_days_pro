import pandas as pd
import streamlit as st
from PIL import Image
import datetime as dt
from dataupdate import Update
from dateutil import relativedelta

icon = Image.open('tslogo.jpg')

# streamlit page configration
st.set_page_config(
    page_icon=icon,
    page_title='Employee Details',
    layout="wide"
)

im = Image.open('thundersoft.png')

excel_data = pd.read_excel("demo2.xlsx")

#-----------------------------------------------------------------------------------#
#accesssing columns from excel sheet
name = list(excel_data["EmployeeName"])
ids = list(excel_data['EmployeeID'])
#
# clint1_names = list(excel_data["Clint Name Proj1"])
# clint2_names = list(excel_data["Clint Name Proj2"])
# clint3_names = list(excel_data["Clint Name Proj3"])
# off_board_date_proj1 = list(excel_data['Project1 Offboarding'])
# off_board_date_proj2 = list(excel_data['Project2 Offboarding'])
# off_board_date_proj3 = list(excel_data['Project3 Offboarding'])

obj = Update()

#----------------------------------------------------------------------------------#

# function for dispaly detilas on streamlit UI and calculating
def details(emp_inp, search_by,period_of_time):
    emp_det = excel_data.loc[excel_data[search_by] == emp_inp]                # to get exact user details DataFrame based on user choice
    on_board_date_proj1 = list(emp_det['Project1 Onboard'])
    on_board_date_proj2 = list(emp_det['Project2 Onboard'])
    on_board_date_proj3 = list(emp_det['Project3 Onboard'])
    off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
    off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
    off_board_date_proj3 = list(emp_det['Project3 Offboarding'])
    join_date = list(emp_det['Joining Date'])

    # varibles for assigning related data
    bench_days = 0
    proj1_days = 0
    proj2_days = 0
    proj3_days = 0
    all_proj =  0
    status = "Bench"

    h1_21_start = dt.datetime.strptime('2021-01-10', '%Y-%m-%d')
    h1_21_end = dt.datetime.strptime('2021-06-10', '%Y-%m-%d')
    h2_21_start = dt.datetime.strptime('2021-06-11', '%Y-%m-%d')
    h2_21_end = dt.datetime.strptime('2021-12-31', '%Y-%m-%d')

    h1_22_start=dt.datetime.strptime('2022-01-10', '%Y-%m-%d')
    h1_22_end=dt.datetime.strptime('2022-06-10', '%Y-%m-%d')
    h2_22_start = dt.datetime.strptime('2022-06-11', '%Y-%m-%d')
    h2_22_end = dt.datetime.strptime('2022-12-31', '%Y-%m-%d')

    def h1_workdays_start(on_board,off_board,h1,h2):
        print('met 78')
        print(on_board,off_board,h1,h2)

        if on_board >= h1 and on_board <= h2 and off_board == 'None':
            return (h2 - on_board).days
        elif (on_board <= h1  and off_board == 'None'):
            print('met 109')
            if h2 > dt.datetime.now():
                return (dt.datetime.now() -h1).days
            else:
                return (h2 - h1).days
        elif on_board >= h1 and on_board <= h2 and off_board >= h2:
            print('met81')
            return (h2 - on_board).days

        elif on_board >= h1 and off_board <= h2:
            print('met83')
            return (off_board - on_board).days
        elif on_board <= h1 and off_board > h2:

            print('met86')
            return (h2 - on_board).days
        elif on_board <= h1 and off_board < h2 and off_board > h1:
            print('met94')
            return (off_board - h1).days

        else :
            print('met 97')
            return 'Employee Not Worked in this Period'
        #return working_days

    # def single_work(on_board,h1,h2):
    #     print('met 102')
    #     print(on_board,h1,h2)
    #     if on_board >= h1 and on_board <= h2:
    #         return (h2 - on_board).days
    #     elif (on_board <= h1 and on_board):
    #         print('met 109')
    #         return h2 - h1
    #     else:
    #         return 'Employee Not Worked in this Period'
    #     #return working_days


    # def h2_workdays_end(on_board,offboard) :
    #     global working_days
    #     if on_board_date_proj1[0] >= h1_22_start and on_board_date_proj1[0] <= h1_22_end:
    #      working_days += h1_21_end - on_board_date_proj1[0]
    #     elif on_board_date_proj1[0] >= h1_22_start and off_board_date_proj1[0] <= h1_22_end:
    #      working_days += off_board_date_proj1[0] - h1_22_start
    #     elif on_board_date_proj1[0] <= h1_22_start and off_board_date_proj1[0] > h1_22_end:
    #      working_days += off_board_date_proj1[0] - on_board_date_proj1[0]


    #------------------------------------------------------------#
    # to debug the code just commentout the print statements you can know which block of code excuted

    times = ['Select Time', '21 H1', '21 H2', "22 H1", "22 H2"]
    try:
        if (join_date[0]) == 'None':
            print('0 if ')
            st.error('Candidate not Onboarded till now')
            if period_of_time != "Select Time":
                all_proj='Employee Not Worked in this Period'
            else:
                all_proj = 'you should select the time'

        elif (on_board_date_proj1[0]) == "None":
            print('1st if')
            bench_days += (dt.datetime.now() - join_date[0]).days
            if period_of_time != "Select Time":
                all_proj = 'Employee Not Worked in this Period'
            else:
                all_proj = 'you should select the time'


        elif (off_board_date_proj1[0]) == 'None' and (on_board_date_proj1[0]) != "None":
            print('2nd if')
            status = "Project 1"
            proj1_days = (dt.datetime.now() - on_board_date_proj1[0]).days
            if period_of_time ==  "21 H1":
                all_proj = h1_workdays_start(on_board_date_proj1[0],off_board_date_proj1[0],h1_21_start,h1_21_end)
            elif period_of_time == '22 H1':
                all_proj = h1_workdays_start(on_board_date_proj1[0],off_board_date_proj1[0], h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj1[0],off_board_date_proj1[0],h2_21_start,h2_21_end)
            elif period_of_time == '22 H2':
                all_proj = h1_workdays_start(on_board_date_proj1[0], off_board_date_proj1[0],h2_22_start, h2_22_end)
            else:
                all_proj = 'you should select the time'
                print('you should select the time')

            # print(type(on_board_date_proj1[0]))
            bench_days += (on_board_date_proj1[0] - join_date[0]).days
        elif (off_board_date_proj1[0]) != "None" and (on_board_date_proj2[0]) == 'None':
            print('3RD IF')
            proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
            bench_days += (dt.datetime.now() - off_board_date_proj1[0]).days
            bench_days += (on_board_date_proj1[0] - join_date[0]).days()
            if period_of_time ==  "21 H1":
                all_proj =h1_workdays_start(on_board_date_proj1[0], off_board_date_proj1[0], h1_21_start, h1_21_end)
            elif period_of_time == '22 H1':
                 all_proj =h1_workdays_start(on_board_date_proj1[0], off_board_date_proj1[0], h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj1[0], off_board_date_proj1[0], h2_21_start, h2_21_end)
            else :
                 all_proj =h1_workdays_start(on_board_date_proj1[0], off_board_date_proj1[0], h2_22_start, h2_22_end)


        elif on_board_date_proj2[0] != "None" and off_board_date_proj2[0] == 'None':
            print('4th if')
            status = "Project 2"
            proj1_days = (off_board_date_proj1[0] - on_board_date_proj1[0]).days
            proj2_days = (dt.datetime.now() - on_board_date_proj2[0]).days
            bench_days += (on_board_date_proj2[0] - off_board_date_proj1[0]).days
            bench_days += (on_board_date_proj1[0] - join_date[0]).days

            if period_of_time ==  "21 H1":
                all_proj = h1_workdays_start(on_board_date_proj2[0],off_board_date_proj2[0],h1_21_start,h1_21_end)
            elif period_of_time == '22 H1':
                all_proj = h1_workdays_start(on_board_date_proj2[0],off_board_date_proj2[0] ,h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0],off_board_date_proj2[0],h2_21_start,h2_21_end)
            elif period_of_time == '22 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0],off_board_date_proj2[0], h2_22_start, h2_22_end)
            else:
                print('you should select the time')
        elif off_board_date_proj2[0] != 'None' and on_board_date_proj3[0] == 'None':
            print('5th if')
            # bench_days += dt.datetime.now() - off_board_date_proj2[0]
            bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
            bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
            bench_days += (dt.datetime.now().date() - off_board_date_proj2[0].date()).days
            proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
            proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days

            if period_of_time == "21 H1":
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h1_21_start, h1_21_end)
            elif period_of_time == '22 H1':
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h2_21_start, h2_21_end)
            elif period_of_time == '22 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h2_22_start, h2_22_end)
            else:
                all_proj= 'You not selected Time'




        elif on_board_date_proj3[0] != 'None' and off_board_date_proj3[0] == "None":
            print('6th if')
            status= "Project3"
            bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
            bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
            bench_days += (on_board_date_proj3[0].date() - off_board_date_proj2[0].date()).days
            proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
            proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
            proj3_days = (dt.datetime.now().date() - on_board_date_proj3[0].date()).days

            if period_of_time == "21 H1":
                all_proj = h1_workdays_start(on_board_date_proj3[0],off_board_date_proj3[0], h1_21_start, h1_21_end)
            elif period_of_time == '22 H1':
                all_proj = h1_workdays_start(on_board_date_proj3[0],off_board_date_proj3[0], h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj3[0],off_board_date_proj3[0], h2_21_start, h2_21_end)
            elif period_of_time == '22 H2':
                all_proj = h1_workdays_start(on_board_date_proj3[0],off_board_date_proj3[0], h2_22_start, h2_22_end)
            else:
                print('you should select the time')


        elif off_board_date_proj3[0] != "None":
            print('7th if')
            bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
            bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
            bench_days += (on_board_date_proj3[0].date() - off_board_date_proj2[0].date()).days
            bench_days += (dt.datetime.now().date() - off_board_date_proj3[0].date()).days
            proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
            proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
            proj3_days = (off_board_date_proj3[0].date() - on_board_date_proj3[0].date()).days

            if period_of_time == "21 H1":
                 all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h1_21_start, h1_21_end)
            elif period_of_time == '22 H1':
                 all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h1_22_start, h1_22_end)
            elif period_of_time == '21 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h2_21_start, h2_21_end)
            elif period_of_time == '22 H2':
                all_proj = h1_workdays_start(on_board_date_proj2[0], off_board_date_proj2[0], h2_22_start, h2_22_end)
            else:
                all_proj = 'You not selected Time'

            if all_proj != int:
                if period_of_time == "21 H1":
                    all_proj = h1_workdays_start(on_board_date_proj3[0], off_board_date_proj3[0], h1_21_start, h1_21_end)
                elif period_of_time == '22 H1':
                    all_proj = h1_workdays_start(on_board_date_proj3[0], off_board_date_proj3[0], h1_22_start, h1_22_end)
                elif period_of_time == '21 H2':
                    all_proj = h1_workdays_start(on_board_date_proj3[0], off_board_date_proj3[0], h2_21_start, h2_21_end)
                elif period_of_time == '22 H2':
                    all_proj = h1_workdays_start(on_board_date_proj3[0], off_board_date_proj3[0], h2_22_start, h2_22_end)
                else:
                    all_proj = 'You not selected Time'

        else:
            print('else')
            pass
    except Exception:
        print(Exception)
        print('An erroe occured in if else block')
    st.write(emp_det) # printing DataFrame on streamlit UI

    #--------------------------------------------------#
    #this two lines code use to if user didn't click the Upadate all button beacuse we are accessing data from updated table otherwise these wo lines should be use

    #diff = relativedelta.relativedelta(dt.datetime.now(), join_date[0])
    #tenure_date = str(diff.years) + "y/" + str(diff.months) + "m/" + str(diff.days) + 'd'

    #------------------------------------------------------#

    lis = ['EmployeeName', 'EmployeeID','Status','Total_Tenure',"Total_Utilization"]     # accesseing column names for showing project days
    if period_of_time =='Select Time':
        for i in emp_det:
            if i == 'Bench Days':
                st.write((i), ":", int(bench_days))
                st.write('Project1 days:', proj1_days)
                st.write('Project2 days:', proj2_days)
                st.write("Project3 days", proj3_days)
                #st.write('Work_days in ',period_of_time,':',all_proj)
            else:
                try:
                    if i in lis:
                        st.write(i, ':', list(emp_det[i])[0])
                except NameError:
                    print(NameError, 'Name not in lis')
    else:
        st.write('Work_days in ', period_of_time, ':', all_proj)
        st.write('Present_Status :' ,status)
        st.write('Total_Tenure', ':', list(emp_det['Total_Tenure'])[0])
        st.write('Total_Utilization', ':', list(emp_det['Total_Utilization'])[0])




#------------------------------------------------------------------------------------------#


# def with_time(emp_inp,search_by,period_of_time):
#     emp_det = excel_data.loc[excel_data[search_by] == emp_inp]  # to get exact user details DataFrame based on user choice
#
#     on_board_date_proj1 = list(emp_det['Project1 Onboard'])
#     on_board_date_proj2 = list(emp_det['Project2 Onboard'])
#     on_board_date_proj3 = list(emp_det['Project3 Onboard'])
#     off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
#     off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
#     off_board_date_proj3 = list(emp_det['Project3 Offboarding'])
#     join_date = list(emp_det['Joining Date'])
#     print('yes')
#     if period_of_time =="21 H1":
#         h1_21_start = dt.datetime.strptime('2021-01-10','%Y-%m-%d')
#         h1_21_end = dt.datetime.strptime('2021-06-10', '%Y-%m-%d')
#         print(h1_21_start)
#         if on_board_date_proj1[0] >= h1_21_start and on_board_date_proj1[0] <= h1_21_end:
#             print('include')
#             pass
#
#







col1, col2, col3 = st.columns([5, 5, 5])
with col1:
    st.image(im)

#---------------------------------------------------------------------------------------------------#
#streamlit part to main UI base don user choice we sending data to the detilas() func and calling exceal update func
ids = ["Select ID"]+ids
name= ["Select Employee Name"] + name
search_by_lis= ['EmployeeName', "EmployeeID"  ]#,"Project_1_going",'Project_2_going','Project_3_going','Complete_Bench']
search_by = st.selectbox('Search By', search_by_lis)
if search_by == 'EmployeeName':
    emp_inp = st.selectbox("Enter Employee details",name)
    period_of_time= st.selectbox("Enter H1 or H2",('Select Time','21 H1','21 H2',"22 H1","22 H2"))

    if st.button('Submit'):
        if (emp_inp == "Select Employee Name"):
            st.error('Please Select The Name')
        else:
            details(emp_inp,'EmployeeName',period_of_time)
    if st.button("Update All"):
        try:
            obj.all_col()
            st.success('you updated all bench days')
        except:
            print('Exception at bench days class calling 1')

else:
    emp_inp = st.selectbox("Enter Employee details", ids)
    period_of_time= st.selectbox("Enter Period Of Time H1 or H2",('Select Time','21 H1','21 H2',"22 H1","22 H2"))

    if st.button('Submit'):
        if (emp_inp == "Select ID"):
            st.error('Please Select ID')
        else:
            details(emp_inp, search_by,period_of_time)
    if st.button("Update All"):
        try:
            obj.all_col()
            st.success('you updated all bench days')
        except:
            print('Except in Bench days class calling 6')







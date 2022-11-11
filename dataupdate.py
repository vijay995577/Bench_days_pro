import pandas
import pandas as pd
import datetime as dt

import streamlit
from dateutil import relativedelta
data=pd.read_excel("demo2.xlsx")
#data = pd.read_excel("demo2.xlsx")
emp_names= list(data["EmployeeName"])

rows_length=(len(emp_names))

class Update:
    def all_col(self):
        for i in range(rows_length):
            if  i> rows_length:
                break
            else:
                emp_name = emp_names[i]
                emp_det = data.loc[data["EmployeeName"] == emp_name]


                on_board_date_proj1 = list(emp_det['Project1 Onboard'])
                on_board_date_proj2 = list(emp_det['Project2 Onboard'])
                on_board_date_proj3 = list(emp_det['Project3 Onboard'])
                off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
                off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
                off_board_date_proj3 = list(emp_det['Project3 Offboarding'])
                join_date = list(emp_det['Joining Date'])

                bench_days = 0
                status= "Bench"
                proj1_days = 0
                proj2_days = 0
                proj3_days = 0

                try:
                    if (join_date[0]) == 'None':
                        print('0 if ')
                        print('Candidate was not Onboarded till now')

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
                        proj2_days = (dt.datetime.now() - on_board_date_proj2[0]).days
                        bench_days += (on_board_date_proj2[0] - off_board_date_proj1[0]).days
                        bench_days += (on_board_date_proj1[0] - join_date[0]).days
                    elif off_board_date_proj2[0] != 'None' and on_board_date_proj3[0] == 'None':
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
                        status= "project3"
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
                    print('Excepiton at if else blocks while bench days updating')
                    #print('An erroe occured in if else block')

                # data.at[i,'Bench Days']= int(bench_days)
                if join_date[0] != "None"   :
                    diff = relativedelta.relativedelta(dt.datetime.now() ,join_date[0])
                    tenure_date=str(diff.years)+"y/"+str(diff.months)+"m/"+str(diff.days)+'d'
                    tenure_days = (dt.datetime.now() - join_date[0]).days
                    uti_days = proj1_days + proj2_days +proj3_days
                    uti_per = (uti_days/tenure_days) * 100
                    data.at[i,'Tenure'] =  tenure_date
                    data.at[i,"Utilization"]= str(round(uti_per))+"%"
                    data.at[i, 'Bench Days'] = int(bench_days)
                    data.at[i, 'Status'] = status

                else:
                    data.at[i,'Tenure'] ="None"
                    data.at[i, 'Utilization'] = "None"
                    data.at[i,'Bench Days'] = "None"
                    data.at[i, 'Status'] = "None"
                    print('Add join date 1st')


                # data.at[i,'Status'] = status
        #print(data)
        data.to_excel("demo2.xlsx",index=False)

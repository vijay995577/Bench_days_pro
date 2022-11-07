import pandas as pd
import datetime as dt
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
                off_board_date_proj1 = list(emp_det['Project1 Offboarding'])
                off_board_date_proj2 = list(emp_det['Project2 Offboarding'])
                join_date = list(emp_det['Joining Date'])

                bench_days = 0
                status= "Bench"
                proj1_days = 0
                proj2_days = 0

                if on_board_date_proj1[0] == "None":
                    bench_days = (dt.datetime.now().date() - join_date[0].date()).days
                    print('1st if')
                elif (off_board_date_proj1[0]) == 'None' and (on_board_date_proj1[0]) != "None":
                    print('2nd if')
                    status= "Project 1"
                    # print(type(on_board_date_proj1[0]))
                    bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                elif (off_board_date_proj1[0]) != "None" and (on_board_date_proj2[0]) == 'None':
                    print('3RD IF')
                    proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
                    bench_days += (dt.datetime.now().date() - off_board_date_proj1[0].date()).days
                    bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days()
                    # print(bench_days)
                elif on_board_date_proj2[0] != "None" and off_board_date_proj2[0] == 'None':
                    print('4th if')
                    status = "Project 2"
                    proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
                    bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
                    bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                elif off_board_date_proj2[0] != 'None':
                    print('5th if')

                    bench_days += (on_board_date_proj2[0].date() - off_board_date_proj1[0].date()).days
                    bench_days += (on_board_date_proj1[0].date() - join_date[0].date()).days
                    bench_days += (dt.datetime.now().date() - off_board_date_proj2[0].date()).days
                    proj2_days = (off_board_date_proj2[0].date() - on_board_date_proj2[0].date()).days
                    proj1_days = (off_board_date_proj1[0].date() - on_board_date_proj1[0].date()).days
                else:
                    print('else')
                    pass
                data.at[i,'Bench Days']= int(bench_days)

                data.at[i,'Status'] = status
        print(data.to_string())
    #all_col()
        data.to_excel("demo2.xlsx",index=False)

#
#
# # print(data.info())
# #
# # new_data=data.loc[data["EmployeeName"]=="Priyanka E"]
# # print(new_data)
# # index=list(new_data.index)[0]
# # data.at[index,'Bench Days']=38
# # print(data.tail(5))
# data.to_excel("demo2.xlsx")
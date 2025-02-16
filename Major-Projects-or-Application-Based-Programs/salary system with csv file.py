# a better/different logic for the same program of salary system is in this code:
# https://github.com/AnmolDixitB13/R/blob/main/salary%20system%20in%20R.txt

"""
Salary System code storing data in csv file

The I/P Section should accept the following details about the employee: 
- name
- monthly base salary
- month & year for which the employee's salary has to be calculated
- no. of leave days the employee took in that month
- the tax deduction (tds).

The O/P Section should display the employee details & following details/calculations - (tds deduction, leave 
deduction, final monthly take home salary) at console & along with this, a copy of the I/P details & the 
calculations should also be sent to the csv file as records.

Note: If the entered month is Feb, the program must find out whether that year's feb was a leap year or not
i.e. no. of days was 28 or 29. This info will be needed while deducting salary if the employee has taken
leave(s).
I have achived this using a function leap() and dictionary days. When a month is entered, the program fetches the days
suitably from the dictionary. If feb is entered as month, the function will analyze whether that year was leap or not and accordingly, the program will fetch no. of days from the dictionary suitably.
"""

# a better/different logic for the same program of salary system is in this code:
# https://github.com/AnmolDixitB13/R/blob/main/salary%20system%20in%20R.txt

import pandas as pd

filepath = '/content/my_sample_data/sal_record.csv'

def leap(year):
  if year%4 != 0:
   #print("Year ", year, " is not a leap year. (Code executed from first if statement)")
   total_days_in_month = days["feb_reg"]

  elif year%100!=0:
   #print("Year ", year, " is a leap year. (Code executed from first elif statement)")
   total_days_in_month = days["feb_leap"]

  elif year%100 == 0 and year%400 == 0:
    #print("Year ", year, " is a leap year. (Code executed from second elif statement)")
    total_days_in_month = days["feb_leap"]
  else:
    #print("Year ", year, " is not a leap year.")
    total_days_in_month = days["feb_reg"]

  return total_days_in_month
  #print("returned value")


days = {
    "jan" : 31,
    "january" : 31,
    "mar" : 31,
    "march" : 31,
    "apr" : 30,
    "april" : 30,
    "may" : 31,
    "jun" : 30,
    "june" : 30,
    "jul" : 31,
    "july" : 31,
    "aug" : 31,
    "august" : 31,
    "sep" : 30,
    "september": 30,
    "oct" : 31,
    "october" : 31,
    "nov" : 30,
    "november" : 31,
    "dec" : 31,
    "december" : 31,
    "feb_reg" : 28,
    "feb_leap" : 29,
    "february_reg" : 28,
    "february_leap" : 29,
}

#################################################

def salary_leaves_taken():

  one_day_salary = monthly_base_sal/total_days_in_month
  leave_days_sal_deduction = one_day_salary*leave_days

  new_monthly_sal = monthly_base_sal - leave_days_sal_deduction

  tds_deduction = tds_per*new_monthly_sal/100
  final_monthly_sal = new_monthly_sal - tds_deduction

  yearly_salary_ctc = monthly_base_sal*12

  return yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal
#################################################

def salary_leaves_not_taken():

  tds_deduction = tds_per*monthly_base_sal/100
  final_monthly_sal = monthly_base_sal - tds_deduction

  yearly_salary_ctc = monthly_base_sal*12

  leave_days_sal_deduction = 0

  return yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal

#################################################

name = input("Enter the employee's name:\t")
while len(name) == 0 or name.isdecimal():
  if len(name) == 0:
    while len(name) == 0:
      print("\nName can't be empty.")
      name = input("Re enter the correct employee's name:\t")

  if name.isdecimal():
    while name.isdecimal():
      print("\nName can't be purely numerical.")
      name = input("Re enter the correct employee's name:\t")

monthly_base_sal = float(input("Enter the monthly base salary of the employee:\t"))
if monthly_base_sal < 0:
  while monthly_base_sal < 0:
    print("\nInvalid Salary. Salary can't be negative.")
    monthly_base_sal = float(input("Re enter the correct monthly base salary of the employee:\t"))

month = input("Enter the month for which the final/take home monthly salary has to be calculated:\t")
year = abs(int(input("Enter the year to which the entered month belongs to:\t")))
"""
abs() method has been used to ensure if the user mistakenly or purposely enters negative year, such as -2024, the program 
will automatically consider the positive value of it.
"""

if(month == 'feb' or month == 'february'):
  total_days_in_month = leap(year)

else:
  total_days_in_month = days[month]

leave_days = int(input("Enter the no. of leave days the employee took in the previous month:\t"))
while leave_days > total_days_in_month or leave_days < 0:
  if leave_days > total_days_in_month:
    while leave_days > total_days_in_month:
      print("\nInvalid Leave Days. Monthly Leave Days > Total Days In Month.")
      leave_days = int(input("Re - enter correctly the no. of leave days the employee took in the previous month:\t"))

  if leave_days < 0:
    while leave_days < 0:
      print("\nInvalid Leave Days. Leave days can't be negative.")
      leave_days = int(input("Re - enter correctly the no. of leave days the employee took in the previous month:\t"))

if monthly_base_sal == 0:
  tds_per = 0
else:
  tds_per = float(input("Enter the TDS as applicable:\t"))
  if tds_per < 0 or tds_per > 25:
    while tds_per < 0 or tds_per > 25:
      print("\nInvalid TDS Deduction Rate. TDS % should be in range 0 - 25 %.")
      tds_per = float(input("Re enter the correct value of TDS as applicable:\t"))

#################################################

#if leaves are taken, so leave days won't be 0 and the statement will be executed

if leave_days:
  yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal = salary_leaves_taken()

else:
  yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal = salary_leaves_not_taken()

#############################################################

print("\n-------------------------------------------------")
print("Name\tMonthly Base\tAnnual CTC\tMonth Leave Days\tDeducted Leave Amount\tTDS %\tTDS Deduction\tFinal Monthly Salary\n")
print(name,"\t",monthly_base_sal,"\t",yearly_salary_ctc,"\t",leave_days,"\t\t\t",leave_days_sal_deduction,"\t\t\t",tds_per,"\t\t",tds_deduction,"\t\t",final_monthly_sal)

df = pd.DataFrame(pd.read_csv(filepath))

sal_data = {
    'Name' : name,
    'Monthly Base' : monthly_base_sal,
    'Annual CTC' : yearly_salary_ctc,
    'Month' : month,
    'Year' : year,
    'Monthly Leaves Taken' : leave_days,
    'Deducted Leave Amount' : leave_days_sal_deduction,
    'TDS %' : tds_per,
    'TDS Deduction' : tds_deduction,
    'Final Monthly Salary' : final_monthly_sal
}

indexx = [0]
sal_df = pd.DataFrame(sal_data, index=indexx)
joint = pd.concat([df, sal_df])
joint.to_csv(filepath)

# a better/different logic for the same program of salary system is in this code:
# https://github.com/AnmolDixitB13/R/blob/main/salary%20system%20in%20R.txt

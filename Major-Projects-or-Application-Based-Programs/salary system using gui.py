"""
In a window, there should be 2 frames, either as a single row or a single column. One frame will be
I/P frame i.e. it will be used to accept employee name, monthly base salary, tax %, to be deducted, 
leaves, etc. The other frame will be used to display the info like tax deductions, leave deductions, 
final monthly takehome salary, etc.

Once the button is pressed after entering the details & displaying the calculated data, the textfields 
should be auto cleared preferably.
"""

import tkinter as tk
from tkinter import messagebox


#########################################################

"""
If the employee has taken leaves, so accordingly, for those days the salary
should be deducted. So, for this purpose we need to know how many days were 
there in that month. So, this info has been stored in the form of key value
pairs in the dictionary.

Secondly, if the month was feb, then we also need to check was it a leap
year's feb or a regular/non - leap year's feb. So, for that also, a 
function has been defined that will be executed only if the user entered
month is feb. 

There are 2 functions to calculate final taken home salary for the month as
entered by the user. One function is when the leaves are taken other is 
executed when no leaves are taken. Anyways, one can merge the 2 functions
and keep one common function for the same.

"""
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


###################################################

def salary_leaves_taken(salary, tds_per, leaves, total_days_in_month):

  one_day_salary = salary/total_days_in_month
  leave_days_sal_deduction = one_day_salary*leaves

  new_monthly_sal = salary - leave_days_sal_deduction

  tds_deduction = tds_per*new_monthly_sal/100
  final_monthly_sal = new_monthly_sal - tds_deduction

  yearly_salary_ctc = salary*12

  return yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal
#################################################

def salary_leaves_not_taken(salary, tds_per):

  tds_deduction = tds_per*salary/100
  final_monthly_sal = salary - tds_deduction

  yearly_salary_ctc = salary*12

  leave_days_sal_deduction = 0

  return yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal


#####################    Setting Screen layout    #####################

window = tk.Tk()

window .geometry("1200x1200")
window.title("Salary System")
scroll_win = tk.Scrollbar(window, relief="raised", orient='vertical', activebackground="blue", highlightbackground='grey')

#scroll_win.pack()
#cannot use geometry manager grid inside . which already has slaves managed by pack


frame1 = tk.Frame(window, bg="blue",background="pink", height=400, width=1250)
frame1.grid(row=0, column=0, padx=10, pady=10)
scroll1 = tk.Scrollbar(frame1, orient='vertical')

frame2 = tk.Frame(window, bg="blue",background="purple", height=400, width=1250)
frame2.grid(row=0, column=1, padx=10, pady=10)
scroll2 = tk.Scrollbar(frame2, orient='vertical')

flag_name = True
flag_sal = True
flag_leaves = True
flag_tds_per = True

global total_days_in_month
global entry_leaves
entry_leaves = tk.Entry(frame1)

var = tk.IntVar()


def reset_textfields():
    entry_leaves.delete(0, tk.END)
    entry_tds.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_monthly_sal.delete(0, tk.END)

"""this function clears the textfields once the results have been 
calculated & displayed. """
#################################################################

def fn():
    print(f"var in fn : {var.get()}")

    if var.get() == 1:
        entry_leaves.config(highlightcolor="Red", highlightbackground="darkBlue", highlightthickness=2, width=40)
        entry_leaves.grid(row=9, column=1, padx=10, pady=10)

    else:
        entry_leaves.grid_remove()
        print("executed else")

######################    Validate user I/Ps    ######################


def validate():

        name = entry_name.get()
        if len(name) == 0:
            messagebox.showwarning("Improper Name", "Name can't be empty. Re enter the name.")
            flag_name = False

        elif name.isdecimal():
            messagebox.showwarning("Improper Name", "Name can't be completely numerical. Re enter the name correctly.")
            flag_name = False

        else:
            flag_name = True

        ##################      Leap year or not    ###################

        try:
            year = int(entry_year.get())

            if entry_month.get().casefold() == 'feb':
                total_days_in_month = leap(year)

            else:
                total_days_in_month = days[entry_month.get().casefold()]
        except:
            messagebox.showinfo("Year Conversion Problem", "Some problem occured while trying to convert 'year' from String to Float. Re enter year & month correctly.")

        ################## Converting String to int/float #############
        try:
            tds_per = float(entry_tds.get())

            if entry_leaves.get() != None:
                 leaves = int(entry_leaves.get())

            else:
                leaves = 0

        except:
            messagebox.showinfo("Conversion problem", "Some problem occured while converting String to Float. Re enter the values of leaves / tds % correctly.")
            leaves = 0
            #break

        ############################

        salary = float(entry_monthly_sal.get())
        if salary < 0:
            messagebox.showwarning("Improper Salary", "Salary can't be negative. Re enter the salary correctly.")
            flag_sal = False

        else:
            flag_sal = True

        ############################

        if leaves < 0:
            messagebox.showwarning("Improper leave days. Leave days can't be negative.")
            flag_leaves = False


        if leaves > total_days_in_month:
            messagebox.showwarning("Improper leave days",
                                   "Leave days can't be more than no. of days in month. Re enter correctly.")
            flag_leaves = False


        elif leaves == None:
            flag_leaves = True

        else:
            flag_leaves = True

        if tds_per < 0 or tds_per > 25:
            messagebox.showwarning("Improper TDS % value", "TDS % should be in range 0 - 25. Re enter TDS % correctly.")
            flag_tds_per = False

        else:
            flag_tds_per = True

        if flag_name and flag_sal and flag_leaves and flag_tds_per:
            print("All ok.")

            if leaves == 0:
                yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal = salary_leaves_not_taken(
                    salary, tds_per)

            else:
                yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal = salary_leaves_taken(
                    salary, tds_per, leaves, total_days_in_month)
        """
        If all the I/Ps are appropriate, only then the function to calculate
        the final takehome salary should be called and only then the values
        should be passed to the function.
        """


        ##########################################
	# print them for reference only

        print(name)
        print(leaves)
        print(tds_per)
        print(salary)
        print(total_days_in_month)

        disp_data(yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal)


#################################################################

def disp_data(yearly_salary_ctc, leave_days_sal_deduction, tds_deduction, final_monthly_sal):

    print("Sal details")
    print(leave_days_sal_deduction)
    print(tds_deduction)
    print(final_monthly_sal)
    print()

    label_Name2 = tk.Label(frame2, text=f"Name: {entry_name.get()}")
    label_Name2.grid(row=4, column=2, padx=10, pady=10)

    label_monthly_sal2 = tk.Label(frame2, text=f"Monthly Base Salary: {entry_monthly_sal.get()}")
    label_monthly_sal2.grid(row=5, column=2, padx=10, pady=10)

    label_annual_ctc = tk.Label(frame2, text=f"Annual CTC: {yearly_salary_ctc}")
    label_annual_ctc.grid(row=6, column=2, padx=10, pady=10)

    label_month_year = tk.Label(frame2, text=f"Month/Year: {entry_month.get()} / {entry_year.get()}")
    label_month_year.grid(row=7, column=2, padx=10, pady=10)

    label_leaves2 = tk.Label(frame2, text=f"Leaves: {entry_leaves.get()}")
    #label_leaves2 = tk.Label(frame2, text=f"Leaves: {ent_leaves}")
    label_leaves2.grid(row=8, column=2, padx=10, pady=10)

    label_leave_deduction = tk.Label(frame2, text=f"Leave Days' Deduction: {leave_days_sal_deduction}")
    label_leave_deduction.grid(row=9, column=2, padx=10, pady=10)

    label_tds_per = tk.Label(frame2, text=f"TDS %: {entry_tds.get()}")
    label_tds_per.grid(row=10, column=2, padx=10, pady=10)

    label_tds_deduction = tk.Label(frame2, text=f"TDS Deduction: {tds_deduction}")
    label_tds_deduction.grid(row=11, column=2, padx=10, pady=10)

    label_final_takehome_sal = tk.Label(frame2, text=f"Final Takehome Salary: {final_monthly_sal}")
    label_final_takehome_sal.grid(row=12, column=2, padx=10, pady=10)

    reset_textfields()

######################   UI of the I/P Section   #######################

label_intro1 = tk.Label(frame1, text="Enter details here", background="white", foreground="black", font=6)
label_intro1.grid(row=2, column=0, padx=10, pady=10)

label_Name = tk.Label(frame1, text="Employee name")
entry_name = tk.Entry(frame1, highlightcolor="Red", highlightbackground="darkBlue",highlightthickness=2, width=40)
label_Name.grid(row=4, column=0, padx=10, pady=10)
entry_name.grid(row=4, column=1, padx=10, pady=10)

label_monthly_sal = tk.Label(frame1, text="Monthly Base Salary")
label_monthly_sal.grid(row=5, column=0, padx=10, pady=10)
entry_monthly_sal = tk.Entry(frame1, highlightcolor="Red", highlightbackground="darkBlue", highlightthickness=2, width=40)
entry_monthly_sal.grid(row=5, column=1, padx=10, pady=10)

label_year = tk.Label(frame1, text="Year")
label_year.grid(row=6, column=0, padx=10, pady=10)
entry_year = tk.Entry(frame1, highlightcolor="Red", highlightbackground="darkBlue",highlightthickness=2, width=40)
entry_year.grid(row=6, column=1, padx=10, pady=10)

label_month = tk.Label(frame1, text="Month")
label_month.grid(row=7, column=0, padx=10, pady=10)
entry_month = tk.Entry(frame1, highlightcolor="Red", highlightbackground="darkBlue",highlightthickness=2, width=40)
entry_month.grid(row=7, column=1, padx=10, pady=10)

label_tds = tk.Label(frame1, text="TDS %")
label_tds.grid(row=8, column=0, padx=10, pady=10)
entry_tds = tk.Entry(frame1, highlightcolor="Red", highlightbackground="darkBlue",highlightthickness=2, width=40)
entry_tds.grid(row=8, column=1, padx=10, pady=10)

cb_leaves = tk.Checkbutton(frame1)
cb_leaves.config(text="Leaves taken ?" , activebackground="red", activeforeground="pink", selectcolor="pink", foreground="black", borderwidth=1, variable=var, command=fn)
cb_leaves.grid(row=9, column=0, padx=10, pady=10)


b = tk.Button(frame1, text="Proceed", activebackground="red", activeforeground="black", background="skyblue", foreground="black", border=1, borderwidth=1, relief="solid", height=1, width=8, command=validate)
b.grid(row=10, column=1, padx=10, pady=10)


##################################################


label_intro2 = tk.Label(frame2, text="Summary", font=6, background="white", foreground="black")
label_intro2.grid(row=2, column=2, padx=10, pady=10)

window.mainloop()

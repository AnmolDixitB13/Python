'''
Accept subject names and store them in a list. In the same order, accept marks in these subjects and store them in 
another list. Depending upon the marks in individual subjects, grade the subjects accordingly. Then find total marks in 
all subjects and then find overall grading and display suitably. 

Ensure that the subject names don't repeat and marks are between 0 and 100 and the no. of subjects should be between 
3 and 10 (you can alter these conditions as per your requirements/wish).
'''


def overall_grading(grade, n_sub, percent):
  i = 0
  passed = True
  while(i < n_sub):
    if(grade[i] == 'F'):
      #if 'F' in grade:
      overall_grade = 'F'
      overall_passing_status = 'F'
      passed = False

      return overall_grade, overall_passing_status
      break
    i += 1

    '''
    Alternative to the above lines of code:
    grade = ['P', 'P', 'P', 'P']

      if 'F' in grade:
        print("yes")

      else:
        print("no")
    '''

  while(passed):
      if 81 <= percent <= 100 :
        overall_grade = 'A'
        overall_passing_status = 'P'

      elif 61 <= percent <= 80 :
        overall_grade = 'B'
        overall_passing_status = 'P'

      elif 41 <= percent <= 60 :
        overall_grade = 'C'
        overall_passing_status = 'P'

      elif 31 <= percent <= 40 :
        overall_grade = 'D'
        overall_passing_status = 'P'

      else:
        overall_grade = 'F'
        overall_passing_status = 'F'

      return overall_grade, overall_passing_status
      break




def subject_grading(marks, n_sub):
  grade = []
  # to store grades in the subjects

  for i in range(n_sub):
    if 81 <=marks[i]<= 100:
      grade.append('A')
      #grade[i] = 'A' #throws error list assignment index out of range

    elif 61 <=marks[i]<= 80:
      #grade[i] = 'B'
      grade.append('B')

    elif 41 <=marks[i]<= 60:
      #grade[i] = 'C'
      grade.append('C')

    elif 31 <=marks[i]<= 40:
      #grade[i] = 'D'
      grade.append('D')

    else:
      #grade[i] = 'F'
      grade.append('F')

  return grade



def calculations(marks, n_sub):
  total_marks_obtained = 0

  for i in range(n_sub):
    total_marks_obtained += marks[i]

  percent = (total_marks_obtained/(100*n_sub))*100

  return total_marks_obtained, percent


sub = []
# to store subjects' names
marks = []
# to store marks in the above subjects
grade = []
# to store grades of the above subjects

print("Welcome to the student portal. Enter the details as prompted.")

while True:
  name = input("Enter the student's name:\t")

  if len(name)==0:
    print("Name can't be empty. Re - enter the name correctly.")
    continue

  elif name.isdecimal()==True:
    print("Name can't be purely numerical. Re - enter the name correctly.")
    continue

  else:
    break

while True:

  n_sub = int(input("Enter the no. of subjects whose marks are to be processed:\t"))
  if n_sub in range(3, 10):
    break
  else:
    print("The no. of subjects should be between 3 and 10. Re - enter the no. of subjects correctly.")
    continue

print("\nEnter the names of the subjects:\n")

i = 0
while i < n_sub:
  temp = input(f"Enter the name of subject {i+1}:\t")

  if temp not in sub and temp.isdecimal() == False and len(temp)!=0:
    sub.append(temp)
    i += 1
  else:
    print(f"Either subject {temp} is already in the list or the name of the subject is improper or is empty.")
    continue


print(f"\nEnter the marks in the {n_sub} subjects.\n")

i = 0
while i < n_sub:
  temp = int(input(f"Enter the marks in subject {sub[i]}:\t"))

  if temp < 0 or temp > 100:
    print(f"Marks should be between 0 and 100. Re enter the marks in the subject {sub[i]}")
    continue

  else:
    marks.append(temp)
    i+=1

total_marks_obtained, percent = calculations(marks, n_sub)
grade = subject_grading(marks, n_sub)
overall_grade, overall_passing_status = overall_grading(grade, n_sub, percent)

print("\n--------------------------------------\n")
print("The student details are as follows.\n")
print("Name: ", name)
print("\n")

print("Subject | Marks out of 100 | Grade")
for i in range(n_sub):

  print(f"{sub[i]}\t\t{marks[i]}\t\t{grade[i]}")

print("\n")
print("Total marks obtained: ", total_marks_obtained)
print("Maximum marks possible: ", n_sub*100)
print("Overall grade: ", overall_grade)
print("Overall passing status: ", overall_passing_status)

if overall_grade != 'F':
  print("Overall percentage: ", percent)

else:
  print("Overall percentage: --")

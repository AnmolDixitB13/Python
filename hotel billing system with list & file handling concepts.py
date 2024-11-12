'''
Hotel Billing System Code which stores the bill in a text file.

I/P Section:
Enter dish name: _____
Enter price of dish dish name: _____
Enter the quantity of the dish dish name: _____

Do you want to add more dishes ? Y/N or y/n ? 

If yes, then repeat the previous lines.
If no, then 

show/display suitable discounts if any & ask user would you like to add some discount percent to the bill ?
If yes, store it in a variable, as it will be required at the time of bill calculation.

If no discount, assign discount as zero percent.

GST has to be taxed or not ?
If yes, ask user about the GST % to be taxed, store in a variable.
If no, then consider GST as zero percent.

Compute & display the bill/receipt to the user containing these details:

Food/Dish	|	Price	|	Quantity	|	Total

Discount %: _____
Discount amount/concession on total bill (including GST if applicable): _____

GST %: _____
GST Amount: _____

Total Bill (after discount/concession): _____

Transfer all these details to a suitable text/word/any other file type as you wish. No need to do this if you
do not want to try / include file handling concepts/file storage facility in your code.
'''

import math
# this import might not be required in some IDE's

def discount_select():
  print("\n\nHere are few discount offers you may select.\n")
  print("1. Flat 2% off")
  print("2. Flat 4% off")
  print("3. Flat 8% off")
  print("4. Any other offer/discount [manually entering discount %]")
  print("Type nil if no offer has to be selected.")

  while 1:
    ans_discount_choice = input("Enter offer details:\t")

    if ans_discount_choice == 'nil':
      discount_per = 0
      break

    elif ans_discount_choice == '1':
      discount_per = 2

    elif ans_discount_choice == '2':
      discount_per = 4

    elif ans_discount_choice == '3':
      discount_per = 8

    elif ans_discount_choice == '4':
      while 1:
        discount_per = float(input("Enter discount %:\t"))

        if discount_per < 0 or discount_per > 100:
          print("Discount can't be less than 0 % or more than 100 %. Re enter the discount % value.")
          continue

        else:
          break

    else:
      print("Invalid choice. Select the correct option.")
      continue

    return discount_per
    break



####################################################

def bill_with_gst(price, quantity, no_dishes, gst_per, discount_per):

    total_bill = 0
    for i in range(no_dishes):
        total_bill += price[i]*quantity[i]

    gst_amt = gst_per*total_bill/100

    total_bill += gst_amt

    if discount_per:
      disc_amt = total_bill*discount_per/100
      total_bill -= disc_amt

    else:
      disc_amt = 0
    return gst_amt, disc_amt, total_bill

#####################  Accepting the data from the user  ###############

dish = []
price = []
quantity = []

i = 0
ans_continue = 'Y'

while ans_continue.casefold() == 'y' :

  temp = input(f"Enter the name of dish {i+1} :\t")
  while len(temp) == 0 or temp.isdecimal():
    if len(temp) == 0:
      while len(temp) == 0:
        print("\nName of the dish can't be empty.")
        temp = input(f"Re enter the name of dish {i+1} :\t")

    if temp.isdecimal():
      while temp.isdecimal():
        print("\nEntire dish name can't be numerical.")
        temp = input(f"Re enter the name of dish {i+1} correctly:\t")

  dish.append(temp)

  temp = int(input(f"Enter the price of {dish[i]} :\t"))
  if temp <= 0:
    while temp <= 0:
      temp = int(input((f"Price can't be 0 or less than 0. Re enter the correct price for the dish {dish[i]}:\t")))

  price.append(temp)

  temp = int(input(f"Enter the quantity of the dish {dish[i]} :\t"))
  if temp <= 0:
    while temp <= 0:
      temp = int(input((f"Quantity can't be 0 or less than 0. Re enter the correct quantity for the dish {dish[i]}:\t")))

  quantity.append(temp)
  i += 1  # dish count increment

  ans_continue = input("Do you want to add more dishes ? Y/N ?\t")

  if ans_continue.casefold() == 'y':
    continue

  elif ans_continue.casefold() == 'n':
    break

  else:
    while(1):

        print("Invalid choice. Enter Y/N")
        ans_continue = input("Do you want to add more dishes ? Y/N ?:\t")

        if ans_continue.casefold() == 'y' or ans_continue.casefold() == 'n' :
          break

        else:
          continue

count = i   # dish count

#print(dish)  # for ref only
#print(price) # for ref only

####################  Discount Offers ##########################

discount_per = discount_select()

#####################  GST Option   ############################

while 1:
  gst_ans = input("\nGST to be taxed ? Y/N :\t")

  if gst_ans.casefold() == 'y' or gst_ans.casefold() == 'n':
    break
  else:
    print("\nInvalid Option selected. Enter Y/N or y/n.")
    continue

if gst_ans.casefold() == 'y':
  while 1:
    gst_per = float(input("Enter the GST % :\t"))
    if gst_per < 0 or gst_per > 28:
      print("GST should be taxed in the range 0 - 28 %. Re enter the correct GST % value.")
      continue
    else:
      break

  gst_amt, disc_amt, total_bill = bill_with_gst(price, quantity, count, gst_per, discount_per)

elif gst_ans.casefold() == 'n':
      gst_per = 0
      total_bill = 0
      gst_amt = 0
      for i in range(count):
          total_bill += price[i]*quantity[i]

      if discount_per:
        disc_amt = total_bill*discount_per/100
        total_bill -= disc_amt

      else:
        disc_amt = 0

#####################  Displaying the data, Printing final bill ############

print("\n\n")
print("Dish name  |  Price  |  Quantity  |  Total\n")
for i in range(count):
  print(f"{dish[i]}\t\t{price[i]}\t\t{quantity[i]}\t\t{(price[i]*quantity[i])}")

print(f"\nDiscount offer type: {discount_per} %")
print("Discount on total bill (including gst if applicable): ", disc_amt)
print("GST %: ", gst_per)
print("GST amount: ", gst_amt)
print("\nTotal bill (including applicable GST if any & with discount if any): ", total_bill)
print("Rounded off Total bill: ", math.floor(total_bill))

##################### Writing the data to the file #########################
with open("bill.txt", "w") as f:
  f.write("\t\tBill\n\n")
  f.write("Dish name  |  Price  |  Quantity  |  Total\n")
  for i in range(count):
    f.write(f"{dish[i]}\t\t{price[i]}\t\t{quantity[i]}\t\t{(price[i]*quantity[i])}\n")
  f.write("\n")
  f.write("-------------------------------------------------------------------------")
  f.write(f"\nDiscount offer type: {discount_per} %")
  f.write(f"\nDiscount on total bill (including gst if applicable): {disc_amt}")
  f.write(f"\nGST %: {gst_per}")
  f.write(f"\nGST amount: {gst_amt}")
  f.write(f"\nTotal bill (including applicable GST if any & with discount if any): {total_bill}")
  f.write(f"\nRounded off Total bill: {math.floor(total_bill)}")

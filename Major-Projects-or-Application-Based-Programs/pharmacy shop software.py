'''
Pharmacy Shop Software

Tasks to be performed
1. add medicines
2. search medicine by sku no/name and / or update medicine details
3. delete medicine 
4. process an order and suitably deduct the stock of the respective medicines
5. get total stock of medicines in stock 

'''

import math
# often, it may not be required to import it

######################## Medicine Addition Section ######################
def add_append_med(sku, med_name, price, med_stock):

  if len(sku) == 0:
    total_medicines_on_list = 0

  else:
    total_medicines_on_list = len(sku)
    print("len(sku)", len(sku))
    print("Total med on list", total_medicines_on_list)

  ans_add = 'Y'

  while ans_add.casefold() == 'y':

    print("Total med in list inside while loop : ", total_medicines_on_list)

    temp = input("Enter the SKU no. of the medicine (alpha numeric SKUs are allowed):\t")
    if temp in sku:
        print(f"Medicine with sku {temp} is already present at the index {sku.index(temp)}. Re enter with a different SKU.")
        continue
    else:
        sku.append(temp)

    temp = input("Enter the medicine name:\t")
    if temp in med_name:
        while temp in med_name:
            print(f"Medicine {temp} is already present at the index {med_name.index(temp)}")
            temp = input(f"Enter a different medicine name bearing the sku {sku[total_medicines_on_list]}:\t")
            continue
    else:
        med_name.append(temp)

    temp = float(input(f"Enter the price of single unit/bottle/strip medicine {med_name[total_medicines_on_list]}:\t"))
    if temp <= 0:
        while temp <= 0:
            print(f"Price can't be negative or zero. Re enter the price for the medicine {med_name[total_medicines_on_list]}")
            temp = float(input(f"Enter the price correctly of the product {med_name[total_medicines_on_list]}:\t"))
    price.append(temp)

    temp = int(input(f"Enter the quantity of the medicine {med_name[total_medicines_on_list]}:\t"))
    if temp < 0:
        while temp < 0:
            print(f"Stock can't be negative. Re enter the quantity of stock for the medicine {med_name[total_medicines_on_list]}")
            temp = int(input(f"Enter the stock correctly of the medicine {med_name[total_medicines_on_list]}:\t"))
    med_stock.append(temp)


    #print(total_medicines_on_list)
    print("\n")

    while 1:
      ans_add = input("Do you want to add more medicine(s) ? Enter Y/N or y/n ?\t")

      if ans_add.casefold() == 'y' or ans_add.casefold() == 'n':
          break
      else:
        print("Invalid choice. Press Y/N or y/n.")
        print("\n")
        continue

    if ans_add.casefold() == 'y':
      print("\n")
      total_medicines_on_list += 1
      continue

    else:
      break

  return sku, med_name, price, med_stock


######################## Medicine Search & Update Section ##########################

def search_med(sku, med_name, price, med_stock):
    ans_update = ' '
    ans_update_item = ' '
    while 1:
        print("\nPress")
        print("1 to search by sku.")
        print("2 to search by product name.")
        print("3 to terminate search.\n")

        ans_choice = input("Enter your product search method:\t")

        if ans_choice == '1':
            search = input("Enter the sku of the product to be searched:\t")

            if search in sku:
                print("Product is present.\n")
                index = sku.index(search)

                print(f"Medicine at the SKU {sku[index]} is {med_name[index]}.")
                print(f"Total stock of the medicine at SKU {search} / medicine name {med_name[index]} is {med_stock[index]} units.")
                print(f"Price of single medicine of {med_name[index]} is {price[index]}.")
                print(f"Total cost of the entire stock of medicine {med_name[index]} in stock is {price[index] * med_stock[index]}.")

                print("\n")
                while(1):
                  ans_update = input("Do you want to update this medicine's details ? Y/N or y/n ?")

                  if ans_update.casefold() == 'y' or ans_update.casefold() == 'n':
                    break

                  else:
                    print("Invalid option selected. Please select the option Y/N or y/n.")
                    continue

                if ans_update.casefold() == 'y':
                  while 1:
                    ans_update_item = input("Update SKU ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = input(f"Enter the new SKU no. of the medicine (alpha numeric SKUs are allowed) with current SKU {sku[index]}:\t")
                      if temp in sku:
                        while temp in sku:
                          print(f"Medicine with sku {temp} is already present at the index {sku.index(temp)}. Re enter with a different SKU.")
                          temp = input(f"Enter the new SKU no. of the medicine (alpha numeric SKUs are allowed) with current SKU {sku[index]}:\t")
                          continue
                      else:
                        sku[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue

                  while 1:
                    ans_update_item = input("Update Name ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = input(f"Enter the new name of the medicine with current Name {med_name[index]}:\t")
                      if temp in med_name:
                        while temp in med_name:
                          print(f"Medicine with name {temp} is already present at the index {med_name.index(temp)}. Re enter with a different Name.")
                          temp = input(f"Enter the new Name of the medicine with current Name {med_name[index]} & current SKU {sku[index]}:\t")
                          continue
                      else:
                        med_name[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                  while 1:
                    ans_update_item = input("Update Price ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = int(input(f"Enter the new price of the medicine {med_name[index]}:\t"))
                      if temp <= 0:
                        while temp <= 0:
                          print(f"Price can't be negative or zero. Re enter the price for the medicine {med_name[index]}")
                          temp = int(input(f"Enter the price correctly of the product {med_name[index]}:\t"))
                      else:
                        price[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                  while 1:
                    ans_update_item = input("Update Stock ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = int(input(f"Enter the new stock of the medicine {med_name[index]}:\t"))
                      if temp < 0:
                        while temp < 0:
                          print(f"Stock can't be negative. Re enter the stock for the medicine {med_name[index]}")
                          temp = int(input(f"Enter the stock correctly of the product {med_name[index]}:\t"))
                      else:
                        med_stock[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                return sku, med_name, price, med_stock
            else:
                print(f"There is no product with the SKU {search}.\n")

        elif ans_choice == '2':
            search = input("Enter the product name of the product to be searched:\t")

            if search in med_name:
                print("Product is present.\n")
                index = med_name.index(search)

                print(f"SKU of the medicine {med_name[index]} is {sku[index]}.")
                print(f"Total stock of {med_name[index]} present is {med_stock[index]}.")
                print(f"Price of single medicine of {med_name[index]} is {price[index]}.")
                print(f"Total cost of the entire stock of medicine {med_name[index]} in stock is {price[index] * med_stock[index]}.")

                while(1):
                  ans_update = input("Do you want to update this medicine's details ? Y/N or y/n ?")

                  if ans_update.casefold() == 'y' or ans_update.casefold() == 'n':
                    break

                  else:
                    print("Invalid option selected. Please select the option Y/N or y/n.")
                    continue

                if ans_update.casefold() == 'y':
                  while 1:
                    ans_update_item = input("Update SKU ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = input(f"Enter the new SKU no. of the medicine (alpha numeric SKUs are allowed) with current SKU {sku[index]}:\t")
                      if temp in sku:
                        while temp in sku:
                          print(f"Medicine with sku {temp} is already present at the index {sku.index(temp)}. Re enter with a different SKU.")
                          temp = input(f"Enter the new SKU no. of the medicine (alpha numeric SKUs are allowed) with current SKU {sku[index]}:\t")
                          continue
                      else:
                        sku[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue

                  while 1:
                    ans_update_item = input("Update Name ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = input(f"Enter the new name of the medicine with current Name {med_name[index]}:\t")
                      if temp in med_name:
                        while temp in med_name:
                          print(f"Medicine with name {temp} is already present at the index {med_name.index(temp)}. Re enter with a different Name.")
                          temp = input(f"Enter the new Name of the medicine with current Name {med_name[index]} & current SKU {sku[index]}:\t")
                          continue
                      else:
                        med_name[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                  while 1:
                    ans_update_item = input("Update Price ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = int(input(f"Enter the new price of the medicine {med_name[index]}:\t"))
                      if temp <= 0:
                        while temp <= 0:
                          print(f"Price can't be negative or zero. Re enter the price for the medicine {med_name[index]}")
                          temp = int(input(f"Enter the price correctly of the product {med_name[index]}:\t"))
                      else:
                        price[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                  while 1:
                    ans_update_item = input("Update Stock ? Y/N or y/n ?\t")
                    if ans_update_item.casefold() == 'y':
                      temp = int(input(f"Enter the new stock of the medicine {med_name[index]}:\t"))
                      if temp < 0:
                        while temp < 0:
                          print(f"Stock can't be negative. Re enter the stock for the medicine {med_name[index]}")
                          temp = int(input(f"Enter the stock correctly of the product {med_name[index]}:\t"))

                      else:
                        med_stock[index] = temp
                        break
                    elif ans_update_item.casefold() == 'n':
                      break
                    else:
                      print("Invalid option selected. Select Y/N or y/n.")
                      continue
                return sku, med_name, price, med_stock

            else:
                print(f"There is no product with the product name {search}.\n")

        elif ans_choice == '3':
            break

        else:
            while (1):
                print("Invalid choice. Press 1/2/3 suitably depending upon your requirements.")
                ans_choice = input("Enter the choice correctly:\t")

                if ans_choice == '1' or ans_choice == '2' or ans_choice == '3':
                    break

                else:
                    continue


######################## Medicine Removal Section ##########################

def remove_med(sku, med_name, price, med_stock):

    total_medicines_on_list = len(sku)
    while 1:
        print("\nPress:")
        print("1 to remove a product by it's SKU")
        print("2 to remove a product by it's name")
        print("3 to terminate the product removal process")

        while 1:
            ans_choice = input("Enter your product removal option:\t")

            if ans_choice == '1' or ans_choice == '2' or ans_choice == '3':
                print("\n")
                break

            else:
                print("Invalid option selected. Select 1/2/3 as per your need(s).")
                continue

        if ans_choice == '1':
            search = input("Enter the SKU of the product to be removed:\t")

            if search in sku:
                index = sku.index(search)

                sku.pop(index)
                med_name.pop(index)
                price.pop(index)
                med_stock.pop(index)
                total_medicines_on_list -= 1
                print(f"Medicine with SKU {search} has been removed successfully.\n")

            else:
                print(f"There is no medicine with the SKU {search}.")

        elif ans_choice == '2':
            search = input("Enter the name of the product to be removed:\t")

            if search in med_name:
                index = med_name.index(search)

                sku.pop(index)
                med_name.pop(index)
                price.pop(index)
                med_stock.pop(index)
                total_medicines_on_list -= 1
                print(f"Meidcine with name {search} has been removed successfully.\n")

            else:
                print(f"There is no medicine with the name {search}.")

        else:
            break

    return sku, med_name, price, med_stock

#################### Order Processing Section ##########################

def order_processing(sku, med_name, price, med_stock):
  total_medicines_on_list = len(sku)
  order_medicine_again = 'Y'
  order_index = 0
  ans_continue = ' '
  bill = 0.0
  total_bill = 0.0
  quantity_ordered = []

  for i in range(total_medicines_on_list):
    temp = 0
    quantity_ordered.append(temp)
    #quantity_ordered[i] = 0
  # initialize all the values in this list to 0

  if total_medicines_on_list == 0:
    print("No medicines in stock to be sold.\n")

  else:
    #while med_stock not None:#for future considerations
      print("Press the index no. to place the order of  a medicine")
      print(f"Index\t\tMedicine\t\tStock\t\tPrice\n\n")

      for i in range(total_medicines_on_list):
        if med_stock[i] > 0:
          print(f"{i}\t\t{med_name[i]}\t\t{med_stock[i]}\t\t{price[i]}")


      while order_medicine_again.casefold() == 'y':
        while 1:
          temp = int(input("Enter the medicine index no. to place it's order:\t"))

          if temp not in range(0, total_medicines_on_list):
            print("Medicine index number error. The entered medicine index number is improper. Enter the correct medicine index no.")
            continue

          else:
            order_index = temp
            break
        ###############################
        while 1:
          temp = int(input(f"Enter the quantity of the medicine {med_name[order_index]} to be purchased:\t"))

          if temp >= 0 and temp <= med_stock[order_index]:
            quantity_ordered[order_index] = temp
            med_stock[order_index] -= temp
            break

          elif temp >= 0 and temp > med_stock[order_index]:
            print(f"The entered quantity for the medicine {med_name[order_index]} exceeds the stock by {temp - med_stock[order_index]} amount.")
            print(f"If you continue with your order, only {med_stock[order_index]} quantity would be placed in order.")

            ans_continue = input(f"Continue with order of {med_name[order_index]} ? Y/N or y/n ?\t")

            while 1:
              if ans_continue.casefold() == 'y':
                quantity_ordered[order_index] = med_stock[order_index]
                med_stock[order_index] = 0
                break

              elif ans_continue.casefold() == 'n':
                break

              else:
                print("Invalid option selected.")
                ans_continue = input("Re enter Y/N or y/n.")
                continue

          else:
            print(f"Quantity can't be negative. Re enter the quantity for the medicine {med_name[order_index]} correctly.")
          break
          # needed to break outer while loop

        while 1:
          order_medicine_again = input("Do you want to place order of any other medicine ? Y/N or y/n ?\t")

          if order_medicine_again.casefold() == 'y' or order_medicine_again.casefold() == 'n':
            break

          else:
            print("Invalid option selected. Re enter Y/N or y/n.")
            continue
        if order_medicine_again.casefold() == 'y':
          continue

        while 1:
          ans_choice = input("Do you want to tax GST to the final bill ? Y/N or y/n ?\t")

          if ans_choice.casefold() == 'y':

              gst_per = float(input("Enter the GST % that has to be taxed ? (Fractional Values allowed)\t"))

              if gst_per < 0 or gst_per > 28:
                print("GST % should be between 0 and 28 %")
                continue

              else:
                break
          elif ans_choice.casefold() == 'n':
            gst_per = 0

          else:
            print("Invalid option selected.")
            continue


        while 1:
          ans_choice = input("Do you want to add concession to the final bill ? Y/N or y/n ?\t")

          if ans_choice.casefold() == 'y':

              disc_per = float(input("Enter the discount % (fractional values allowed):\t"))

              if disc_per < 0 or disc_per >100 :
                print("Concession can't be negative or more than 100 %. Re enter the discount value correctly.")
                continue

              else:
                break

          elif ans_choice.casefold() == 'n' :
            disc_per = 0
            break

          else:
            print("Invalid option selected.")
            continue



        for i in range(total_medicines_on_list):
          bill += quantity_ordered[i]*price[i]

        gst_amt = gst_per*bill/100
        bill_with_gst = bill + gst_amt

        disc_amt = disc_per*bill_with_gst/100
        total_bill = bill_with_gst - disc_amt

        print("\n-----------------------------------------------------------")
        print("Medicines | Price | Quantity | Total\n")

        for i in range(len(sku)):
          if quantity_ordered[i] != 0:
            print(f"{med_name[i]}\t{price[i]}\t{quantity_ordered[i]}\t{price[i]*quantity_ordered[i]}")

        print("Bill without GST & without Concession: ", bill)
        print("GST %: ", gst_per)
        print("GST Amount: ", gst_amt)
        print("Bill with GST (if applicable): ", bill_with_gst)
        print("Concession %: ", disc_per)
        print("Concession Amount: ",disc_amt)
        print("Bill after deducting Concession: ", total_bill)
        print("Bill after rounding off: ",math.floor(total_bill))

        for i in range(len(sku)):
          quantity_ordered[i] = 0
        # Re - initialize the values in this list to 0 for the next customer



########################################################################

sku = []
med_name = []
price = []
med_stock = []

quantity_ordered = []
total_price_of_commodity = []

total_medicines_on_list = 0

gst_per = 0.0
disc_per = 0.0

print("Enter the list of the medicines and the their details as & when prompted.\n")

sku, med_name, price, med_stock = add_append_med(sku, med_name, price, med_stock)

#################### Operation Selection Option ###########################
while 1:
    print("Press:")
    print("1 to search a medicine/to get an existing medicine details and/or update an existing medicine details.")
    print("2 to remove a medicine.")
    print("3 to get total stock / record of all the medicines on the list (whether in or out of stock).")
    print("4 to add new medicine on the list.")
    print("5 to process an order")

    ans_choice = input("Enter your work:\t")

    if ans_choice == '1':
      if len(sku) == 0:
        print("There are no medicines to search from.")
      else:
        search_med(sku, med_name, price, med_stock)

    elif ans_choice == '2':
      if len(sku) == 0:
        print("The stock is empty. There are no medicines to remove.")
      else:
        sku, med_name, price, med_stock = remove_med(sku, med_name, price, med_stock)

    elif ans_choice == '3':
      if len(sku) == 0:
        print("The stock is empty.")

      else:
        grand_total = 0

        print("\n----------------------------------------------------------")
        print("SKU  |  Name  |  Price  |  Stock  |  Total\n")
# replace quantity ordered by stock
        for i in range(len(sku)):#used len(sku) instead of total_medicines_on_list
            print(f"{sku[i]}  {med_name[i]}  {price[i]}  {med_stock[i]}  {price[i]*med_stock[i]}")
            grand_total += price[i] * med_stock[i]

        print("Total cost of all the goods in stock is ", grand_total, ".\n")

    elif ans_choice == '4':
      sku, med_name, price, med_stock = add_append_med(sku, med_name, price, med_stock)

    elif ans_choice == '5':
      if len(sku) == 0:
        print("There are no medicines on the list to order from.")

      else:
        order_processing(sku, med_name, price, med_stock)

    else:
        while 1:
            print("Invalid input. Re enter your choice.")
            ans_choice = input("Enter your work 1/2/3/4/5:\t")

            if ans_choice == '1' or ans_choice == '2' or ans_choice == '3' or ans_choice == '4' or ans_choice == '5':
                break

            else:
                continue

# this can be looped for automation
# other features can be added here



'''
Billing Stock System

I/P Section:
Enter sku no of the product: 
Enter name no of the product: 
Enter the quantity of the product: 
Enter the price of the single piece/quantity of the product: 

O/P Section:
1. To search a product (by sku or name)
2. To Remove a product (by sku or name)
3. To get/retrieve total stock present

'''

def search_prod(sku, prod_name, quantity, price, prod_count):
    while 1:
        print("\nPress")
        print("1 to search by sku")
        print("2 to search by product name")
        print("3 to terminate search\n")

        ans_choice = input("Enter your product search choice:\t")

        if ans_choice == '1':
            search = input("Enter the sku of the product to be searched.")

            if search in sku:
                print("Product is present.\n")
                index = sku.index(search)

                print(f"Product at the sku {sku[index]} is : {prod_name[index]}")
                print(f"Quantity of {prod_name[index]} present in stock is : {quantity[index]}")
                print(f"Price of single product of {prod_name[index]} is : {price[index]}")
                print(f"Total cost of the product {prod_name[index]} in stock is : {price[index] * quantity[index]}")

            else:
                print(f"There is no product with the SKU {search}.\n")

        elif ans_choice == '2':
            search = input("Enter the product name of the product to be searched.")

            if search in prod_name:
                print("Product is present.\n")
                index = prod_name.index(search)

                print(f"SKU of the product {prod_name[index]} is : {sku[index]}")
                print(f"Quantity of {prod_name[index]} present in stock is : {quantity[index]}")
                print(f"Price of single product of {prod_name[index]} is : {price[index]}")
                print(f"Total cost of the product {prod_name[index]} in stock is : {price[index] * quantity[index]}")

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


######################## Remove a Product Section ##########################

# remove by name, sku no

def remove_prod(sku, prod_name, quantity, price, prod_count):
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
                prod_name.pop(index)
                quantity.pop(index)
                price.pop(index)
                prod_count -= 1
                print(f"Product with SKU {search} has been removed successfully.\n")

            else:
                print(f"There is no product with the SKU {search}.")

        elif ans_choice == '2':
            search = input("Enter the name of the product to be removed:\t")

            if search in prod_name:
                index = prod_name.index(search)

                sku.pop(index)
                prod_name.pop(index)
                quantity.pop(index)
                price.pop(index)
                prod_count -= 1
                print(f"Product with Product Name {search} has been removed successfully.\n")

            else:
                print(f"There is no product with the name {search}.")

        else:
            break
    return sku, prod_name, quantity, price, prod_count

########################################################################

sku = []
prod_name = []
quantity = []
price = []
total_price_of_commodity = []
ans_add = 'Y'
prod_count = 0

print("Enter the list of the products and the their details as & when prompted.\n")

while ans_add == 'Y' or ans_add == 'y':

    
    while True:
        temp = input("Enter the sku no. of the product (alpha numeric skus are allowed):\t")
        if temp in sku:
          print(f"Product with sku {temp} is already present at the index {sku.index(temp)}")
          # index coming 1 less 
          continue

        else:
          sku.append(temp)
          break

    while True:
      temp = input("Enter the product name:\t")
      #if temp in prod_name:
      if temp in prod_name:
          print(f"Product with name {temp} is already present at the index {prod_name.index(temp)}")
          temp = input(f"Enter a different product name for the product with sku {sku.pop()}:\t")
          continue
          #code repeats here once extra
      else:
          prod_name.append(temp)
          break

    temp = int(input(f"Enter the quantity of the product {prod_name[prod_count]}:\t"))
    if temp < 0:
        while temp < 0:
            print(f"Quantity can't be negative. Re enter the quantity for the product {prod_name[prod_count]}")
            temp = int(input(f"Enter the quantity correctly of the product {prod_name[prod_count]}"))
    quantity.append(temp)

    temp = int(input(f"Enter the price of the product {prod_name[prod_count]}:\t"))
    if temp < 0:
        while temp < 0:
            print(f"Price can't be negative or zero. Re enter the quantity for the product {prod_name[prod_count]}")
            temp = int(input(f"Enter the price correctly of the product {prod_name[prod_count]}"))
    price.append(temp)

    prod_count += 1
    print(f"Product count: {prod_count}")
    print("\n")

    ans_add = input("Do you want to add more product(s) ? Enter Y/N or y/n ?\t")
    if ans_add == 'Y' or ans_add == 'y':
        print("\n")
        continue

    elif ans_add == 'N' or ans_add == 'n':
        break
    else:
        while 1:
            print("Invalid choice. Press Y/N or y/n.")
            ans_add = input("Do you want to add more product(s) ? Y/N or y/n ?\t")

            if ans_add == 'Y' or ans_add == 'y' or ans_add == 'N' or ans_add == 'n':
                break
            else:
                print("\n")
                continue

#################### Search / Remove Product Option ###########################
while 1:
    print("Press:")
    print("1 to search a product.")
    print("2 to remove a product.")
    print("3 to get total stock record.")

    ans_choice = input("Enter your work:\t")

    if ans_choice == '1':
        search_prod(sku, prod_name, quantity, price, prod_count)

    elif ans_choice == '2':
        sku, prod_name, quantity, price, prod_count = remove_prod(sku, prod_name, quantity, price, prod_count)

    elif ans_choice == '3':
        grand_total = 0

        print("\n----------------------------------------------------------")
        print("SKU  |  Name  |  Price  |  Quantity  |  Total\n")

        #for i in range(prod_count):	# throws error list index out of bounds
        for i in range(len(sku)):
            print(f"{sku[i]}  {prod_name[i]}  {price[i]}  {quantity[i]}  {price[i] * quantity[i]}")
            grand_total += price[i] * quantity[i]

        print("Total cost of all the goods in stock is ", grand_total, ".\n")

    else:
        while 1:
            print("Invalid input. Re enter your choice.")
            ans_choice = input("Enter your work 1/2/3:\t")

            if ans_choice == '1' or ans_choice == '2' or ans_choice == '3':
                break

            else:
                continue

# this can be looped for automation
# other features can be added here

######################## Product Search Section ##########################

# search by name, sku


################### Displaying the final lists #######################

print(sku)
print(prod_name)
print(quantity)
print(price)
print(prod_count)

# cannot unpack non-iterable NoneType object at line 78

#########################################################################
# Future scope / possible improvements for this program
# 
# 1. prod_count can be substituted by len(sku) or by len(name) or even by len(price) or len(quantity) in loops if using 
# prod_count throws 'list index out of bounds error'
# 2. suitable exception handling can be used if needed
# 

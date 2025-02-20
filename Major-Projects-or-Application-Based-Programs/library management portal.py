# library management portal using list within dictionaries

"""
A library program to perform the following tasks:
1. Add a member
2. Remove a member
3. Add a book
4. Remove a book
5. Issue a book
6. Return a book
7. Get the list of all the available books in the library
8. Get the list of all the books borrowed by a member member
9. Get the list of all the books which have been borrowed by some or the other library member
10. To modify book details
11. To modify user/library member details
12. To get the list of all the member that have pending fines
13. To search a book by title name
14. To search a book by author name
15. To search a book by isbn
16. To search a member by member id
17. To search a menber by member name
18. To extend a book's period
19. To exit the program

Constraints:
1. A member cannot borrow more than 3 books at once
2. Validate data before entering into the record
3. Suitable fines if book not returned/re - issued within 15 days
    If the delay in returning/re - issuing book ranges from 1 - 10 days, fine of rupees 1 per day will 
    be charged. From 11th - 20th day, fine of rupees 2 per day will be charged. Later on, fine of 
    rupees 5 per day will be charged.

Program working:

1. Lend - check whether the member is registered - has he/she taken more than 3 books - not eligible - else
eligible - check book is present or not - lend - decrease count of book by 1 - add to lend record - vice
versa for returning book

2. Book to be entered into records - check isbn is unique - quantity is not negative

3. Member to be entered - ensure member id is unique and ensure that the id does not exist in records
that are already present.

"""

from datetime import datetime

class Methods:
    # m = Methods()

    dict_book_details = {
        'book_isbn': [],
        'book_name': [],
        'author_name': [],
        'book_qty': []
    }

    dict_member_details = {
        'm_name': [],
        'm_id': [],
        'books_already_borrowed': [],
        'pending_fine': []
    }

    dict_lend_return = {
        'book_isbn': [],
        'book_name': [],
        'm_id': [],
        'm_name': [],
        'book_issue_date': []
    }

    def addMember(self):
        temp_member_name = ""
        temp_member_id = ""
        print("Enter the details of the new member to be added to the library membership as & when prompted.\n")
        try:
            while 1:
                temp_member_name = input("Enter the new member's name:\t")

                if len(temp_member_name.strip()) == 0:
                    print("Name can't be empty. Re enter the appropriate name of the new member to be added.")
                    continue

                elif not all(c.isalpha() or c.isspace() for c in temp_member_name.strip()):
                    print("Name is improper. Re enter the appropriate name of the new member to be added.")
                    continue

                else:
                    Methods.dict_member_details['m_name'].append(temp_member_name.strip())
                    break

            while 1:
                temp_member_id = input(f"Enter the unique member ID of the new member {temp_member_name} [alphanumeric id allowed]:\t")

                if temp_member_id.strip() in Methods.dict_member_details['m_id']:
                    print(
                        f"The entered member ID is not unique. It is present in the records. Re enter a different member ID for the new member {temp_member_name}")
                    continue

                elif len(temp_member_id.strip()) == 0:
                    print(
                        f"Member ID can't be empty. Re enter the appropriate member ID for the new member {temp_member_name}.")
                    continue

                else:
                    Methods.dict_member_details['m_id'].append(temp_member_id.strip())
                    break

            Methods.dict_member_details['books_already_borrowed'].append(0)
            Methods.dict_member_details['pending_fine'].append(0)

            print(f"New user has been successfully added with the Memeber ID {temp_member_id}.")

        except ValueError as v:
            print("Some problem occurred with the input...")
            print(v)
            print("Last parametre was possibly couldn't be added because of the above mentioned problem. You may add it using the update feature or delete the record and then re - enter the record with the correct credentials.")

        except TypeError as t:
            print("Some problem occurred with the input...")
            print(t)
            print("Last parametre was possibly couldn't be added because of the above mentioned problem. You may add it using the update feature or delete the record and then re - enter the record with the correct credentials.")

    ####

    def addBook(self):
        temp_book_name = ""
        temp_book_isbn = ""
        temp_book_author = ""
        temp_book_qty = 0
        print("Enter the details of the new book to be added to the library list as & when prompted.\n")

        try:
            while 1:
                temp_book_isbn = input(f"Enter the new book's isbn (alphanumeric IDs are allowed):\t")
                if temp_book_isbn.strip() in Methods.dict_book_details['book_isbn']:
                    print(
                        f"Book with this id {temp_book_isbn.strip()} already exists in the listed books & is associated with "
                        f"the book "
                        f"{Methods.dict_book_details['book_name'][Methods.dict_book_details['book_isbn'].index(temp_book_isbn)]}")
                    continue

                elif len(temp_book_isbn.strip()) == 0:
                    print("Book id can't be empty. Re enter the appropriate & unique book id.")
                    continue

                else:
                    Methods.dict_book_details['book_isbn'].append(temp_book_isbn.strip())
                    break

            while 1:
                temp_book_name = input(f"Enter the title of the book with the isbn {temp_book_isbn}:\t")

                if len(temp_book_name.strip()) == 0:
                    print("Book name can't be empty. Re enter the appropriate name.")
                    continue

                else:
                    Methods.dict_book_details['book_name'].append(temp_book_name.strip())
                    break

            while 1:
                temp_book_author = input(f"Enter the name of the author for the book {temp_book_name}:\t")

                if len(temp_book_author.strip()) == 0:
                    print("Author name can't be empty. Enter the appropriate name.")
                    continue

                else:
                    Methods.dict_book_details['author_name'].append(temp_book_author.strip())
                    break

            while 1:
                temp_book_qty = int(input(f"Enter the quantity for the book {temp_book_name}:\t"))

                if temp_book_qty < 0:
                    print("Quantity can't be negative. Enter zero if it is out of stock/not available. Enter the "
                          "appropriate name.")
                    continue

                else:
                    Methods.dict_book_details['book_qty'].append(temp_book_qty)
                    break

            print(f"New book has been successfully added into library records with the Book ID {temp_book_isbn}.")

        except ValueError as v:
            print("Some problem occurred with the input...")
            print(v)
            print("Last parametre was possibly couldn't be added because of the above mentioned problem. You may add it using the update feature or delete the record and then re - enter the record with the correct credentials.")

        except TypeError as t:
            print("Some problem occurred with the input...")
            print(t)
            print("Last parametre was possibly couldn't be added because of the above mentioned problem. You may add it using the update feature or delete the record and then re - enter the record with the correct credentials.")

    ####

    def removeBook(self):
        try:
            temp_book_id = ""

            temp_book_id = input("Enter the isbn of the book that has to be removed from the library list:\t")

            if temp_book_id not in Methods.dict_book_details['book_isbn']:
                print(f"There is no book with this book ID {temp_book_id}.")

            else:
                ind = Methods.dict_book_details['book_isbn'].index(temp_book_id)

                Methods.dict_book_details['book_isbn'].pop(ind)
                temp_name = Methods.dict_book_details['book_name'].pop(ind)
                Methods.dict_book_details['author_name'].pop(ind)
                Methods.dict_book_details['book_qty'].pop(ind)

                print(
                    f"Book with book isbn {temp_book_id} & title {temp_name} has been successfully removed from the library list.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    ####

    def lendBook(self):
        # person is member & has < 3 books
        # book exists in record & qty > 0
        # dec count by 1 in its qty
        # modify/update member details i.e. inc books borrowed by 1
        temp_id = ""
        temp_b_id = ""
        ind = 0
        temp_date = ""

        try:
            temp_id = input("Enter the member id of the library member:\t")

            if temp_id not in Methods.dict_member_details['m_id']:
                print(
                    f"The person with the member id {temp_id} is not yet registered in the library as a library member.")

            ind = Methods.dict_member_details['m_id'].index(temp_id)
            if Methods.dict_member_details['books_already_borrowed'][ind] >= 3:
                print(
                    "The library member has already been issued 3 books. A library member can borrow & retain atmost 3 books at a time.")

            else:
                print(f"Library member with id {temp_id} can be issued a book.")

                temp_date = input(
                    "Enter book issue date in the format yyyy-mm-dd format, along with the same delimetre (hyphen):\t")
                act_date = datetime.strptime(temp_date, "%Y-%m-%d").date()

                temp_b_id = input("Enter the book id which has to be issued:\t")

                if temp_b_id not in Methods.dict_book_details['book_isbn']:
                    print(f"There is no book with the book id {temp_b_id}.")

                else:
                    ind = Methods.dict_book_details['book_isbn'].index(temp_b_id)
                    temp_name = Methods.dict_book_details['book_name'][ind]

                    temp_qty = Methods.dict_book_details['book_qty'][ind]

                    if temp_qty == 0:
                        print("There are no copies of this book available as of now.")

                    else:
                        Methods.dict_book_details['book_qty'][ind] -= 1

                        ind3 = Methods.dict_member_details['m_id'].index(temp_id)
                        Methods.dict_member_details['books_already_borrowed'][ind3] += 1
                        memb_name = Methods.dict_member_details['m_name'][ind3]

                        Methods.dict_lend_return['book_isbn'].append(temp_b_id)
                        Methods.dict_lend_return['book_name'].append(temp_name)
                        Methods.dict_lend_return['m_id'].append(temp_id)
                        Methods.dict_lend_return['m_name'].append(memb_name)
                        Methods.dict_lend_return['book_issue_date'].append(act_date)

                        print("Book has been issued to the library member.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    ####

    def extendBook(self):
        n = 0
        try:
            temp_b_id = input("Enter the book isbn of the book whose issue period has to be extended:\t")
            temp_m_id = input("Enter the member id to whom the book has been issued:\t")

            if len(temp_b_id) == 0:
                print("Book id can't be empty.")

            if len(temp_m_id) == 0:
                print("Member id can't be empty.")

            elif temp_b_id not in Methods.dict_book_details['book_isbn']:
                print(f"Book id mismatch... There is no book with this book id {temp_b_id}.")

            n = len(Methods.dict_lend_return['book_isbn'])
            for i in range(n):

                if Methods.dict_lend_return['m_id'][i] == temp_m_id and Methods.dict_lend_return['book_isbn'][i] == temp_b_id:

                    print("Record found.")
                    temp_lend_date = Methods.dict_lend_return['book_issue_date'][i]
                    Methods.dict_lend_return['book_issue_date'][i] = datetime.now().date()

                    date_diff = datetime.now().date() - temp_lend_date
                    days = date_diff.days
                    delay_in_returning_book = days - 15
                    if days >= 16:
                        if delay_in_returning_book in range(11):
                            print(f"Delay of {delay_in_returning_book} days in returning book.")
                            print("A fine of 1 Rupees per day will be charged.")
                            print(f"Total fine on this book is {(delay_in_returning_book) * 1} Rupees.")
                            print("\n")
                            while 1:
                                print("Press:")
                                print("1. to pay fine now itself")
                                print("2. to add this fine in your pending fine records")
                                try:
                                    ans = int(input("Enter the task"))

                                    if ans == 1:
                                        print("Fine received.")
                                        break

                                    elif ans == 2:
                                        fine = delay_in_returning_book * 1
                                        ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                        Methods.dict_member_details['pending_fine'][ind] += fine
                                        print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                        break

                                    else:
                                        print("Invalid option entered.")
                                        continue

                                except ValueError as v:
                                    print("Some problem occurred...")
                                    print(v)

                                except TypeError as t:
                                    print("Some problem occurred...")
                                    print(t)

                        elif delay_in_returning_book in range(11, 21):
                            print(f"Delay of {delay_in_returning_book} days in returning book.")
                            fine = 10 + ((delay_in_returning_book - 10) * 2)
                            print(
                                "A fine of 2 Rupees per day will be charged from 11th day to the last day, for 1st 10 days, it is Rupees 1.")
                            print(f"Total fine on this book is {fine} Rupees.")
                            print("\n")
                            while 1:
                                print("Press:")
                                print("1. to pay fine now itself")
                                print("2. to add this fine in your pending fine records")
                                try:
                                    ans = int(input("Enter the task"))

                                    if ans == 1:
                                        print("Fine received.")
                                        break

                                    elif ans == 2:
                                        ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                        Methods.dict_member_details['pending_fine'][ind] += fine
                                        print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                        break

                                    else:
                                        print("Invalid option entered.")
                                        continue

                                except ValueError as v:
                                    print("Some problem occurred...")
                                    print(v)

                                except TypeError as t:
                                    print("Some problem occurred...")
                                    print(t)

                        elif delay_in_returning_book >= 21:
                            print(f"Delay of {delay_in_returning_book} days in returning book.")
                            fine = 10 + 20 + ((delay_in_returning_book - 20) * 5)
                            print(
                                "A fine of 5 will be charged after 20 days, 1 rupee for 1st 10 days and 2 rupees for 11th - 20th days, per day will be charged.")
                            print(f"Total fine on this book is {fine} Rupees.")
                            print("\n")
                            while 1:
                                print("Press:")
                                print("1. to pay fine now itself")
                                print("2. to add this fine in your pending fine records")
                                try:
                                    ans = int(input("Enter the task"))

                                    if ans == 1:
                                        print("Fine received.")
                                        break

                                    elif ans == 2:
                                        ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                        Methods.dict_member_details['pending_fine'][ind] += fine
                                        print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                        break

                                    else:
                                        print("Invalid option entered.")
                                        continue

                                except ValueError as v:
                                    print("Some problem occurred...")
                                    print(v)

                                except TypeError as t:
                                    print("Some problem occurred...")
                                    print(t)

                    else:
                        print("No fine on this book.")

                    print("Book has been successfully re - issued to the library member.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def returnBook(self):
        # enter book id of the book to be returned, check was it lended ? if yes,
        # then it can be returned
        # inc count by 1 in its qty in dict_book_author_qty
        # modify/update member details i.e. dec books borrowed by 1
        # remove details from lend_return dict ?
        temp_b_id = ""
        b_name = ""
        ind = 0
        temp_m_id = ""

        try:
            temp_b_id = input("Enter the book isbn of the book which has to be returned:\t")
            temp_m_id = input("Enter the member id whose book has to be returned:\t")

            if len(temp_b_id) == 0:
                print("Book id can't be empty.")

            elif len(temp_m_id) == 0:
                print("Member id can't be empty.")

            elif temp_b_id not in Methods.dict_book_details['book_isbn']:
                print(f"Book id mismatch... There is no book with this book id {temp_b_id}.")

            elif temp_m_id not in Methods.dict_member_details['m_id']:
                print(f"Member id mismatch... There is no registered member with this member id {temp_m_id}.")

            else:
                for i in range(len(Methods.dict_lend_return['book_isbn'])):

                    if Methods.dict_lend_return['m_id'][i] == temp_m_id and Methods.dict_lend_return['book_isbn'][i] == temp_b_id:
                        # ind = Methods.dict_lend_return['book_isbn'].index(temp_b_id)
                        Methods.dict_lend_return['book_isbn'].pop(i)
                        b_name = Methods.dict_lend_return['book_name'].pop(i)
                        temp_m_id = Methods.dict_lend_return['m_id'].pop(i)
                        Methods.dict_lend_return['m_name'].pop(ind)
                        temp_lend_date = Methods.dict_lend_return['book_issue_date'].pop(i)

                        ind = Methods.dict_book_details['book_name'].index(b_name)
                        Methods.dict_book_details['book_qty'][ind] += 1

                        ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                        Methods.dict_member_details['books_already_borrowed'][ind] -= 1

                        date_diff = datetime.now().date() - temp_lend_date
                        days = date_diff.days
                        delay_in_returning_book = days - 15
                        if days >= 16:
                            if delay_in_returning_book in range(11):
                                print(f"Delay of {delay_in_returning_book} days in returning book.")
                                print("A fine of 1 Rupees per day will be charged.")
                                print(f"Total fine on this book is {(delay_in_returning_book) * 1} Rupees.")
                                print("\n")
                                while 1:
                                    print("Press:")
                                    print("1. to pay fine now itself")
                                    print("2. to add this fine in your pending fine records")
                                    try:
                                        ans = int(input("Enter the task"))

                                        if ans == 1:
                                            print("Fine received.")
                                            break

                                        elif ans == 2:
                                            fine = delay_in_returning_book * 1
                                            ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                            Methods.dict_member_details['pending_fine'][ind] += fine
                                            print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                            break

                                        else:
                                            print("Invalid option entered.")
                                            continue

                                    except ValueError as v:
                                        print("Some problem occurred...")
                                        print(v)

                                    except TypeError as t:
                                        print("Some problem occurred...")
                                        print(t)

                            elif delay_in_returning_book in range(11, 21):
                                print(f"Delay of {delay_in_returning_book} days in returning book.")
                                fine = 10 + ((delay_in_returning_book - 10) * 2)
                                print(
                                    "A fine of 2 Rupees per day will be charged from 11th day to the last day, for 1st 10 days, it is Rupees 1.")
                                print(f"Total fine on this book is {fine} Rupees.")
                                print("\n")
                                while 1:
                                    print("Press:")
                                    print("1. to pay fine now itself")
                                    print("2. to add this fine in your pending fine records")
                                    try:
                                        ans = int(input("Enter the task"))

                                        if ans == 1:
                                            print("Fine received.")
                                            break

                                        elif ans == 2:
                                            ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                            Methods.dict_member_details['pending_fine'][ind] += fine
                                            print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                            break

                                        else:
                                            print("Invalid option entered.")
                                            continue

                                    except ValueError as v:
                                        print("Some problem occurred...")
                                        print(v)

                                    except TypeError as t:
                                        print("Some problem occurred...")
                                        print(t)

                            elif delay_in_returning_book >= 21:
                                print(f"Delay of {delay_in_returning_book} days in returning book.")
                                fine = 10 + 20 + ((delay_in_returning_book - 20) * 5)
                                print(
                                    "A fine of 5 will be charged after 20 days, 1 rupee for 1st 10 days and 2 rupees for 11th - 20th days, per day will be charged.")
                                print(f"Total fine on this book is {fine} Rupees.")
                                print("\n")
                                while 1:
                                    print("Press:")
                                    print("1. to pay fine now itself")
                                    print("2. to add this fine in your pending fine records")
                                    try:
                                        ans = int(input("Enter the task"))

                                        if ans == 1:
                                            print("Fine received.")
                                            break

                                        elif ans == 2:
                                            ind = Methods.dict_member_details['m_id'].index(temp_m_id)
                                            Methods.dict_member_details['pending_fine'][ind] += fine
                                            print(f"Fine of Rupees {fine} added to the member's pending fine record")
                                            break

                                        else:
                                            print("Invalid option entered.")
                                            continue

                                    except ValueError as v:
                                        print("Some problem occurred...")
                                        print(v)

                                    except TypeError as t:
                                        print("Some problem occurred...")
                                        print(t)

                        else:
                            print("No fine on this book.")

                        print("Book has been successfully returned back to library.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    ####

    def booksAvailableForLending(self):

        try:
            if len(Methods.dict_book_details['book_isbn']) == 0:
                print("There are no registered books in the library as of now.")

            else:
                print("Book name\tAuthor name\tNo.of copies available for issuing")
                for i in range(len(Methods.dict_book_details['book_name'])):
                    if Methods.dict_book_details['book_qty'][i] != 0:
                        print(
                            f"{Methods.dict_book_details['book_name'][i]}\t{Methods.dict_book_details['author_name'][i]}\t{Methods.dict_book_details['book_qty'][i]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)
        ####

    def borrowedBooksOfAMember(self):
        # if dict_lend_return['m_id'][i] == temp_m_id, print(details at i)
        temp_m_id = ""
        found = False
        try:
            temp_m_id = input("Enter the member id of the member whose book borrow record has to be found out:\t")

            if temp_m_id not in Methods.dict_member_details['m_id']:
                print(f"There is no member with this member id {temp_m_id}.")

            else:
                print("Book id\tBook name")
                n = len(Methods.dict_lend_return['m_id'])

                for i in range(n):
                    if Methods.dict_lend_return['m_id'][i] == temp_m_id:
                        print(f"{Methods.dict_lend_return['book_isbn'][i]}\t{Methods.dict_lend_return['book_name'][i]}")
                        found = True

                if not found:
                    print("This library member has not borrowed any book(s).")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    ####

    # __________________________________________________

    def listOfBooksIssued(self):

        try:
            n = len(Methods.dict_lend_return['book_isbn'])

            if n == 0:
                print("As of now, no book(s) have been issued to any of the library member(s).")

            else:
                print("\nHere is the list of all the library books that have been issued or the ones that are currently with the library members.\n")
                print(f"\nIn all, {n} records were found.\n")
                print("Issue Date\tMember ID\tMember Name\tBook ID\tBook Name\n")
                for i in range(len(Methods.dict_lend_return['book_isbn'])):
                    print(f"{Methods.dict_lend_return['book_issue_date'][i]}\t{Methods.dict_lend_return['m_id'][i]}\t{Methods.dict_lend_return['m_name'][i]}\t{Methods.dict_lend_return['book_isbn'][i]}\t{Methods.dict_lend_return['book_name'][i]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def allBooksInLibrary(self):

        try:
            if len(Methods.dict_book_details['book_isbn']) == 0:
                print("There are no registered books in the library as of now.")

            else:
                print("Book ISBN\tBook name\tAuthor name\tNo. of copies in library\n")

                for i in range(len(Methods.dict_book_details['book_isbn'])):
                    print(
                        f"{Methods.dict_book_details['book_isbn'][i]}\t{Methods.dict_book_details['book_name'][i]}\t{Methods.dict_book_details['author_name'][i]}\t{Methods.dict_book_details['book_qty'][i]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def listOfAllLibraryMembers(self):
        try:
            n = len(Methods.dict_member_details['m_id'])
            if n == 0:
                print("There are no registered library members as of now.")

            else:
                print("Here is the list of all the registered library members.\n")
                print("Membership ID\tMember name\tBooks borrowed now\tPending fine\n")

                for i in range(len(Methods.dict_member_details['m_id'])):
                    print(
                        f"{Methods.dict_member_details['m_id'][i]}\t{Methods.dict_member_details['m_name'][i]}\t{Methods.dict_member_details['books_already_borrowed'][i]}\t{Methods.dict_member_details['pending_fine'][i]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def listOfAllMembersWhoHaveTakenBook(self):
        try:
            n = len(Methods.dict_member_details['m_id'])
            if n == 0:
                print("There are no registered members in the library members' list.")

            else:
                print("\nHere is the list of library members who have taken/borrowed at least 1 book from the library.")
                print(f"\nIn all, {n} records were found.\n")
                print("Membership ID\tMember name\tNo of books issued to them\n")

                for i in range(n):
                    if Methods.dict_member_details['books_already_borrowed'][i] != 0:
                        print(
                            f"{Methods.dict_member_details['m_id'][i]}\t{Methods.dict_member_details['m_name'][i]}\t{Methods.dict_member_details['books_already_borrowed'][i]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def membersWithPendingFines(self):

        not_found = True
        count = 0
        total_pending_fine = 0
        n = len(Methods.dict_member_details['m_id'])

        if n == 0:
            print("There are no registered library members.")

        else:
            print("Member id\tMember name\tFine amount\n")
            for i in range(n):
                if Methods.dict_member_details['pending_fine'][i] != 0:
                    not_found = False
                    count += 1
                    total_pending_fine += Methods.dict_member_details['pending_fine'][i]
                    print(
                        f"{Methods.dict_member_details['m_id'][i]}\t{Methods.dict_member_details['m_name'][i]}\t{Methods.dict_member_details['pending_fine'][i]}")

        if not_found:
            print("There are no library members with pending fines.")

        else:
            print(f"In all, {count} records were found.")
            print(f"Total pending fine for the library is {total_pending_fine}.")

    def removeMember(self):
        # accept m_id, check whether member is registered or not
        # if pending books or fines, acc can't be deleted, else delete/cancel
        # library membership
        temp_m_id = ""
        ind = 0
        try:

            if len(Methods.dict_member_details['m_id']) == 0:
                print("There are no registered members in the library members' list.")

            else:

                temp_m_id = input(
                    "Enter the membership id of the library member whose membership has to be cancelled/revoked ?")

                if temp_m_id not in Methods.dict_member_details['m_id']:
                    print(f"There is no library member with this membership id {temp_m_id}.")

                else:
                    if temp_m_id in Methods.dict_lend_return['m_id']:  # or Methods.dict_member_details['pending_fine']
                        print(
                            f"Library member {temp_m_id} has still not returned some library book(s). So, his/her account/membership can't be deleted/revoked.")

                    else:
                        print(
                            f"Library member {temp_m_id} has no books to be returned. So, his/her account/membership can "
                            f"be deleted/revoked.")

                        ind = Methods.dict_member_details['m_id'].index(temp_m_id)

                        Methods.dict_member_details['m_id'].pop(ind)
                        Methods.dict_member_details['m_name'].pop(ind)
                        Methods.dict_member_details['books_already_borrowed'].pop(ind)
                        Methods.dict_member_details['pending_fine'].pop(ind)

                        print(
                            f"Member with member id {temp_m_id} has been successfully removed from the library membership list.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def updateBookDetails(self):

        temp_b_id = ""
        ind = 0
        ans = ""
        new_ = ""
        new_qty = 0

        if len(Methods.dict_book_details['book_isbn']) == 0:
            print("There are no books in the library list.")

        else:
            try:
                temp_b_id = input("Enter the isbn of the book that has to be updated:\t")

                if temp_b_id not in Methods.dict_book_details['book_isbn']:
                    print(f"There is no book with this isbn {temp_b_id}.")

                else:
                    ind = Methods.dict_book_details['book_isbn'].index(temp_b_id)

                    while 1:
                        ans = input("Update the book's isbn ? Y/N or y/n ?\t")
                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_ = input("Enter the new isbn of the book:\t")

                            if new_.strip() in Methods.dict_book_details['book_isbn']:
                                print("New isbn entered already exists in the record. Enter another unique isbn.")
                                continue

                            elif len(new_.strip()) == 0:
                                print("New isbn can't be empty.")
                                continue

                            else:
                                Methods.dict_book_details['book_isbn'][ind] = new_
                                print("Book isbn updated successfully.\n")
                                break

                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input("Update the book's title ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_ = input("Enter the new title of the book:\t")

                            if len(new_.strip()) == 0:
                                print("New title can't be empty.")
                                continue

                            else:
                                Methods.dict_book_details['book_name'][ind] = new_
                                print("Book name updated successfully.\n")
                                break
                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input("Update the book's author name ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_ = input("Enter the new author of the book:\t")

                            if len(new_.strip()) == 0:
                                print("New author name can't be empty.")
                                continue

                            if not all(c.isalpha() or c.isspace() for c in new_.strip()):
                                print("Improper name entered.")
                                continue

                            else:
                                Methods.dict_book_details['author_name'][ind] = new_
                                print("Author name updated successfully.\n")
                                break
                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input(
                            "Update the book's quantity i.e. no. of copies present in the library ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_qty = int(input("Enter the new quantity for the book:\t"))

                            if new_qty < 0:
                                print(
                                    "The quantity can't be negative. Enter zero if no. copies of this book are available in the library.")
                                continue

                            else:
                                Methods.dict_book_details['book_qty'][ind] = new_qty
                                print("Book quantity updated successfully.\n")
                                break

                        else:
                            print("Invalid option entered.")
                            continue

            except ValueError as v:
                print("Some problem occurred... couldn't update the last parametre of the book")
                print(v)

            except TypeError as t:
                print("Some problem occurred... couldn't update the last parametre of the book")
                print(t)

            except IndexError as ie:
                print("Some problem occurred... couldn't update the last parametre of the book")
                print(ie)

    def updateMemberDetails(self):
        temp_m_id = ""
        temp_m_name = ""
        temp = ""
        ind = 0
        ans = ""
        new_ = 0

        if len(Methods.dict_member_details['m_id']) == 0:
            print("There are no registered members in the library members' list.")

        else:
            try:
                temp_m_id = input("Enter the member id of the library member whose details are to be updated:\t")

                if temp_m_id not in Methods.dict_member_details['m_id']:
                    print(f"There is no registered member with this member id {temp_m_id}.")

                else:
                    ind = Methods.dict_member_details['m_id'].index(temp_m_id)

                    while 1:
                        ans = input("Update the member id of the registered library member ? Y/N or y/n ?")
                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            temp = input("Enter the new member id of the library member (alpha numeric id allowed):\t")

                            if temp.strip() in Methods.dict_member_details['m_id']:
                                print("New entered member id already exists in the record.")
                                continue

                            elif len(temp.strip()) == 0:
                                print("New id can't be empty.")
                                continue

                            else:
                                Methods.dict_member_details['m_id'][ind] = temp.strip()
                                print("Member id updated successfully.\n")
                                break

                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input("Update the member's name ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            temp = input("Enter the new name of the member:\t")

                            if len(temp.strip()) == 0:
                                print("New member name can't be empty.")
                                continue

                            elif not all(c.isalpha() or c.isspace() for c in temp.strip()):
                                print("Member name can't be alphanumeric or purely numeric.")
                                continue

                            else:
                                Methods.dict_member_details['m_name'][ind] = temp.strip()
                                print("Member name updated successfully.\n")
                                break
                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input("Update the no. of books borrowed record ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_ = int(input("Enter the no. of books the member has borrowed:\t"))

                            if new_ < 0 or new_ > 3:
                                print("Books borrowed can't be negative or more than 3.")
                                continue

                            else:
                                Methods.dict_member_details['books_already_borrowed'][ind] = new_
                                print("Member's book borrow record updated successfully.\n")
                                break
                        else:
                            print("Invalid option entered.")
                            continue

                    while 1:
                        ans = input(
                            "Update the member's pending fine record (total pending fine) ? Y/N or y/n ?\t")

                        if ans.casefold() == 'n':
                            break

                        elif ans.casefold() == 'y':
                            new_ = float(input("Enter the new updated/adjusted fine for this library member:\t"))

                            if new_ < 0:
                                print(
                                    "Pending fine can't be negative. Enter zero (0) if the member is not liable for any fine or the member has cleared off all the fines he/she had.")
                                continue

                            else:
                                Methods.dict_member_details['pending_fine'][ind] = new_
                                print("Member fine updated successfully.\n")
                                break

                        else:
                            print("Invalid option entered.")
                            continue

            except ValueError as v:
                print("Some problem occurred... couldn't update the last parametre of the member")
                print(v)

            except TypeError as t:
                print("Some problem occurred... couldn't update the last parametre of the member")
                print(t)

            except IndexError as ie:
                print("Some problem occurred... couldn't update the last parametre of the member")
                print(ie)

    def readAllMembers(self):
        try:
            n = len(Methods.dict_member_details['m_id'])
            if n == 0:
                print("There are no registered members in the library members' list.")

            else:
                print("Member ID\tMember name\tBooks borrowed\tPending fine\n")
                for i in range(n):
                    print(
                        f"{Methods.dict_member_details['m_id'][i]}\t{Methods.dict_member_details['m_name'][i]}\t{Methods.dict_member_details['books_already_borrowed'][i]}\t{Methods.dict_member_details['pending_fine'][i]}")

                print(f"In all, {n} records were found.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def searchMemberById(self):
        temp_m_id = ""
        ind = 0

        try:
            temp_m_id = input("Enter the member id whose details are to be found out:\t")

            if len(temp_m_id.strip()) == 0:
                print("Member id can't be empty")

            elif temp_m_id.strip() not in Methods.dict_member_details['m_id']:
                print(f"There is no registered member with this member id {temp_m_id}.")

            else:
                ind = Methods.dict_member_details['m_id'].index(temp_m_id.strip())
                print("Member ID\tMember name\tNo. of books borrowed\tPending fine\n")
                print(f"{Methods.dict_member_details['m_id'][ind]}\t{Methods.dict_member_details['m_name'][ind]}\t{Methods.dict_member_details['books_already_borrowed'][ind]}\t{Methods.dict_member_details['pending_fine'][ind]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def searchMemberByName(self):
        temp_m_name = ""
        ind = 0

        try:
            temp_m_name = input("Enter the member name whose details are to be found out:\t")

            if len(temp_m_name.strip()) == 0:
                print("Member name can't be empty")

            elif temp_m_name.strip() not in Methods.dict_member_details['m_name']:
                print(f"There is no registered member with this member name {temp_m_name}.")

            else:
                ind = Methods.dict_member_details['m_name'].index(temp_m_name.strip())
                print("Member ID\tMember name\tNo. of books borrowed\tPending fine\n")
                print(
                    f"{Methods.dict_member_details['m_id'][ind]}\t{Methods.dict_member_details['m_name'][ind]}\t{Methods.dict_member_details['books_already_borrowed'][ind]}\t{Methods.dict_member_details['pending_fine'][ind]}")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def searchBookByTitle(self):
        temp_title = ""
        count = 0

        try:
            temp_title = input("Enter the book title / word or phrase in the title / subject on which the book has to be searched:\t")

            if len(temp_title.strip()) == 0:
                print("Book title can't be empty.")

            # elif any(temp_title.strip() in temp for temp in Methods.dict_book_details['book_name']):
            else:
                print("Book ISBN\tBook name\tAuthor name\tNo. of copies available\n")
                for i in range(len(Methods.dict_book_details['book_isbn'])):
                    if temp_title.strip().lower() in (Methods.dict_book_details['book_name'][i]).lower():
                        count += 1
                        print(f"{Methods.dict_book_details['book_isbn'][i]}\t{Methods.dict_book_details['book_name'][i]}\t{Methods.dict_book_details['author_name'][i]}\t{Methods.dict_book_details['book_qty'][i]}")

            if count == 0:
                 print(f"There is no book with this name / keyword / on this subject {temp_title} in the library.")

            else:
                print(f"In all, {count} records were found.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def searchBookByAuthor(self):
        temp_author = ""
        count = 0

        try:
            temp_author = input(
                "Enter the book author name whose books are to be searched:\t")

            if len(temp_author.strip()) == 0:
                print("Book author name can't be empty.")

            else:
                print("Book ISBN\tBook name\tAuthor name\tNo. of copies available\n")
            # elif any(temp_author.strip() in temp for temp in Methods.dict_book_details['author_name']):
                for i in range(len(Methods.dict_book_details['book_isbn'])):
                    if temp_author.strip().lower() in (Methods.dict_book_details['author_name'][i]).lower():
                        count += 1
                        print(
                            f"{Methods.dict_book_details['book_isbn'][i]}\t{Methods.dict_book_details['book_name'][i]}\t{Methods.dict_book_details['author_name'][i]}\t{Methods.dict_book_details['book_qty'][i]}")

            if count == 0:
                print(f"There are no books of this author {temp_author} in the library.")

            else:
                print(f"In all, {count} records were found.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)

    def searchBookByISBN(self):
        temp_isbn = ""
        count = 0

        try:
            temp_isbn = input(
                "Enter the ISBN of the book to be searched:\t")

            if len(temp_isbn.strip()) == 0:
                print("Book ISBN can't be empty.")

            else:
                print("Book ISBN\tBook name\tAuthor name\tNo. of copies available\n")
                #elif any(temp_isbn.strip() in temp for temp in Methods.dict_book_details['book_isbn']):
                for i in range(len(Methods.dict_book_details['book_isbn'])):
                    if temp_isbn.strip().lower() == (Methods.dict_book_details['book_isbn'][i]).lower():
                        count += 1
                        print(
                        f"{Methods.dict_book_details['book_isbn'][i]}\t{Methods.dict_book_details['book_name'][i]}\t{Methods.dict_book_details['author_name'][i]}\t{Methods.dict_book_details['book_qty'][i]}")

            if count == 0:
                print(f"There are no books with this ISBN {temp_isbn}.")
            else:
                print(f"In all, {count} records were found.")

        except ValueError as v:
            print("Some problem occurred...")
            print(v)

        except TypeError as t:
            print("Some problem occurred...")
            print(t)

        except IndexError as ie:
            print("Some problem occurred...")
            print(ie)


class Execution:

    def __init__(self):
        self.m = Methods()

    def executeProgram(self):
        task = 0

        while 1:
            print("\nWelcome to library portal\n")
            print("Press:")
            print("1. to add a new book in the library list")
            print("2. to remove a book from the library list")
            print("3. to register a new member in the library")
            print("4. to borrow a book from the library")
            print("5. to return a book back to the library")
            print("6. to extend a book's issue period")
            print("7. to get the list of all the available books in the library")
            print("8. to get the list of books borrowed by a library member")
            print("9. to get the list of all the books that have been borrowed by/lended to any/all of the library members")
            print("10. to remove a member from the library membership")
            print("11. to get the list of all the registered library members")
            print("12. to modify/update book details")
            print("13. to modify/update member details (including fine clearance)")
            print("14. to get the list of all the members who have pending fine")
            print("15. to search a member by the member id")
            print("16. to search a member by the name")
            print("17. to search books by the title name")
            print("18. to search books by the author name")
            print("19. to search books by the isbn")
            print("20. to exit the program")

            try:
                task = int(input("Enter your task:\t"))

            except ValueError as v:
                print("Some problem occurred with the input...")
                print(v)

            except TypeError as t:
                print("Some problem occurred with the input...")
                print(t)

            if task == 1:
                self.m.addBook()

            elif task == 2:
                self.m.removeBook()

            elif task == 3:
                self.m.addMember()

            elif task == 4:
                self.m.lendBook()

            elif task == 5:
                self.m.returnBook()

            elif task == 6:
                self.m.extendBook()

            elif task == 7:
                # list of available books in library
                self.m.allBooksInLibrary()

            elif task == 8:
                # books borrowed by a library member
                self.m.borrowedBooksOfAMember()

            elif task == 9:
                # list of books borrowed by all
                self.m.listOfAllMembersWhoHaveTakenBook()

            elif task == 10:
                # to remove a member from the library membership
                self.m.removeMember()

            elif task == 11:
                self.m.readAllMembers()

            elif task == 12:
                # to modify book details
                self.m.updateBookDetails()

            elif task == 13:
                self.m.updateMemberDetails()
            # to modify member details

            elif task == 14:
                self.m.membersWithPendingFines()

            elif task == 15:
                self.m.searchMemberById()
            # search a member by member id

            elif task == 16:
                self.m.searchMemberByName()
            # search a member by member name

            elif task == 17:
                self.m.searchBookByTitle()
            # search a book by title

            elif task == 18:
                self.m.searchBookByAuthor()
            # search a book by author name

            elif task == 19:
                self.m.searchBookByISBN()
            # search a book by isbn

            elif task == 20:
                # to exit the program
                break


class CommenceProgram:

    def __init__(self):
        print("Program commenced.")
        e = Execution()
        e.executeProgram()
        print("\nProgram stopped.")


if __name__ == "__main__":
    CommenceProgram()
# this begins the execution of the program


"""
Future scope/improvements:

1. The need of file handling: once the program is stopped/exited, the data in the
dictionary is lost, so it is essential to use/incorporate suitable file handling
mechanisms to store data, before exiting the program.

2. Or, instead of file handling, one can go for a suitable UI & Backend for this 
program. The use of backend, by & large eliminates the need of file handling.

3. Try finding better way of data handling i.e. without using dictionaries if
possible.

4. try eliminating the use of dictionary/list if possible, i.e. read, write, 
update & delete transactions should happen straight from the file/backend itself.

5. Currently, the fine clearance is also defined within the method that deals 
with updating the member details. However, for this task, i.e. for member fine,
a separate method can be defined for better ease of operation for the end user.

6. tolower() ensures better matching & offers more user friendly approach to the users
to search records based on names/isbn, without having to worry about the case while searching
the records. It can be incorporated at other places also, if I forgot to do in this program.

7. Storing history / old transactions will be easier if a backend like SQL is used. With SQL,
one can make 4 data tables, 1 for each of the below mentioned tasks:
i. Book record: to store details of the books present / listed in library 
ii. Member record: to store details of the library members
iii. Books currently issued: to store records of books that have been issued to the library 
members
iv. Book issue history: to store old records i.e., once an issued book has been returned back 
to library, the issuing details / issuing record of this book should be moved from table
mentioned in point ' iii ' to the table mentioned in this point, point ' iv '. This will act 
as the history of all the issuings of the library books.

8. When the book issue period of an issued book is about to expire, about 2 - 3 days before
this, an email reminder can be sent to the member's email id reminding him/her that he/she
has to either return the book or get it re - issued. I suppose again, even for this task, a 
backend like SQL is required.

"""


"""
This program demonstrates how one can perform CRUD operations on CSV files using Pandas library.

A CSV file contains usernames & corresponding passwords. Design a program in python using pandas to:
1. add a new username / userid - password pair into the CSV file
2. read the password corresponding to a username from the CSV file
3. update a password corresponding to a username in the CSV file
4. update a username in the CSV file
5. delete a username - password pair from the CSV file

"""

import pandas as pd
import os


def add():

    data = {
        'username': ['ghi'],
        'password': ['pass_ghi']
    }

    new_df = pd.DataFrame(data)

    if os.path.exists('records.csv'):

        existing_df = pd.read_csv('records.csv')
        updated_df = pd.concat([existing_df, new_df], ignore_index=True)
    else:
        # If the file does not exist, use the new data
        updated_df = new_df

    updated_df.to_csv('records.csv', index=False)


def read():
    find = input("Enter username whose password has to be searched:\t")
    if os.path.exists('records.csv'):

        existing_df = pd.read_csv('records.csv')

        print(f"{existing_df['password'][existing_df['username'] == find].iloc[0]}")
    # iloc[0] ensures index/record no. of the password is not printed
    else:
        # If the file does not exist, use the new data
        print("Either file does not exist or the record does not exist")


def upd_pass():
    u_name = input("Enter the username / userid whose password has to be updated:\t")

    if os.path.exists('records.csv'):

        data = pd.read_csv('records.csv')

        # if u_name in data['username']:
        # this logic doesn't work
        if (data['username'] == u_name).any():
            new_pass = input(f"Enter new password for the account with u_name {u_name}:\t")
            # data['password'][data['username'] == u_name] = new_pass
            # this logic is correct but doesn't work
            data.loc[data['username'] == u_name, 'password'] = new_pass
            data.to_csv('records.csv')

        else:
            print(f"There is no userid with this name {u_name}.")

    else:
        print("File does not exists.")


def upd_uname():
    u_name = input("Enter the username / userid that has to be updated:\t")

    if os.path.exists('records.csv'):

        data = pd.read_csv('records.csv')

        # if u_name in data['username']:
        # this logic doesn't work
        if (data['username'] == u_name).any():
            new_uname = input(f"Enter new username for the account with u_name {u_name}:\t")
            # data['username'][data['username'] == u_name] = new_pass
            # this logic is correct but doesn't work
            data.loc[data['username'] == u_name, 'username'] = new_uname
            data.to_csv('records.csv')

        else:
            print(f"There is no userid with this name {u_name}.")

    else:
        print("File does not exists.")


def delete():
    if os.path.exists('records.csv'):
        df = pd.read_csv('records.csv')

        u_name = input("Enter the username whose account has to be deleted:\t")

        # if u_name in df['username']:
        # this logic doesn't work
        if (df['username'] == u_name).any():
            updated_df = df[df['username'] != u_name]
            updated_df.to_csv('records.csv', index=False)
            print(f"Deleted user: {u_name}")

        else:
            print(f"There is no record with this username {u_name}.")

    else:
        print("File does not exist.")


def executeProgram():
    inp = 0
    while 1:
        print("Welcome to CSV file handling program\n")
        print("Press:")
        print("1. to add a new username - password pair in the record")
        print("2. to read password corresponding to a username from the record")
        print("3. to update password")
        print("4. to update username")
        print("5. to delete a username - password pair from the record")
        print("6. to stop the program")

        inp = int(input("\nEnter your work:\t"))

        if inp == 1:
            add()

        elif inp == 2:
            read()

        elif inp == 3:
            upd_pass()

        elif inp == 4:
            upd_uname()

        elif inp == 5:
            delete()

        elif inp == 6:
            break

        else:
            print("Invalid option no. entered.")

if __name__ == '__main__':
    executeProgram()

"""
Future scope / improvements:

1. Input from user can be accepted i.e. username & password in the add() function.

2. Exception handling while asking user to enter the no. of task to be performed and / or where 
ever required.

3. Before updating password corresponding to a userid, program should ask for the old/current 
password and then ask for new. If the old/current password entered by the user matches with the 
one in the record corresponding to the userid, the password can be updated, else can't be updated.

4. Similarly, while updating the userid / username, ask the current password. If the password 
matches the one present in records corresponding to the userid / username, then the username can be 
updated, else it can't be updated.

5. Password strength checks can be implemented, to check len. of password, presence/absence of digits, 
special characters, etc.

I haven't implemented points 1 - 5 because in this program I wanted to practice & demonstrate csv file 
handling basic crud operations in pandas and not the robustness / logic of operations, that's the reason I 
didn't implement points 1 - 5.

"""

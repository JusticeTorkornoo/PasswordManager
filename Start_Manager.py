import Account
import Account_Search
import Update_Username
import Update_Password
import Update_Website
import Delete_Account
import time
import Delete_All
import Show_Accounts
import os

#                                                                                  #
# The "restart() abstraction is here so when other abstractions end they start the #
# "Start_manager".start() abstraction again                                        #
#                                                                                  #

def restart():
    start()


#                                                                        #
# The "start" abstraction is where all the other abstractions dtart from #
#                                                                        #

def start():
    os.system('cls')
    answer = input("Choose a number from the options below\n1. Make a new account\n2. Delete an account\n3. Update an account\n4. Show your accounts\n5. Delete all accounts\n6. Search accounts\n")

    if "1" == answer:
        os.system('cls')
        Account.newAccount()

    elif answer == "2":
        os.system('cls')
        Delete_Account.deleteAccount()

    elif answer == "3":
        os.system('cls')
        answer = input("Choose a number from the options below\n1. Update a password\n2. Update a username\n3. Update a website\n")
        
        if "1" in answer:
            os.system('cls')
            Update_Password.password()

        if "2" in answer:
            os.system('cls')
            Update_Username.username()

        if "3" in answer:
            os.system('cls')
            Update_Website.website()

    elif answer == "4":
        os.system('cls')
        Show_Accounts.accounts()

    elif answer == "5":
        os.system('cls')
        Delete_All.deleteAll()

    elif answer == "6":
        os.system('cls')
        Account_Search.search()

    elif answer == "exit":
        os.system('cls')
        print("Exiting...")

    else:
        print("\nThat is not an option")
        time.sleep(1.5)

        print("\nRestarting...")
        time.sleep(1.5)
        os.system('cls')
        restart()
import sqlite3
import Start_Manager
import time
import os

#                                                               #
# This abstraction's role is to delete all data in the database #
#                                                               #

def deleteAll():
    answer = input("Are you sure you want to delete all your passwords?\n")

    if answer == "y" or answer == "yes":
        print("\nDeleting all accounts...\n")
        time.sleep(3)

    #                                                                                                    #
    # the variable "conn" was made so you dont have to type in "sqlite3.connect('PasswordManager.db')"   #
    # every time you wanted to connect to the database. The variable "c" was made to shorten the command #
    # connecting to the database even more when setting the cursor where you want to start entering data #
    # to the database                                                                                    #
    #                                                                                                    # 

        conn = sqlite3.connect('PasswordManager.db')
        c = conn.cursor()

        #                                                                                           #
        # "SELECT * FROM PasswordManager" means that SQlite will select all the data in the databse # 
        # The for loop is there to traverse through the whole database to print all the accounts in #
        # the database                                                                              #
        #                                                                                           #

        c.execute("SELECT * FROM PasswordManager")

        #                                                                                           #
        # "DELETE FROM PasswordManager" means that SQlite will delete all data in the databse       #
        #                                                                                           #

        c.execute("DELETE FROM PasswordManager")

        #                                                                   #
        # "conn.commit()" will save the previous action in the database and #
        # "conn.close()" closes the database so no unwanted data enters the #
        # database on accident                                              #
        #                                                                   #

        conn.commit()
        conn.close()
        print("All accounts deleted")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()

    else:
        print("\nSystem wipe cancelled")
        time.sleep(2.5)
        os.system('cls')
        Start_Manager.start()
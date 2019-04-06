import sqlite3
import Start_Manager
import time
import os

#                                                                                           #
# This abstraction was created to have the ability to show all the accounts in the database #
#                                                                                           #

def accounts():

    count = 0

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

    c.execute("SELECT * FROM PasswordManager ORDER BY Website")
    print("Website                     Username                         Password")
    print()
    for row in c.fetchall():
        count = count + 1
        print("{:25}   {:30}   {:81}".format(row[0], row[1], row[2]))

    if count > 0:
        time.sleep(1.5)
        input("\nPress ENTER to go back to main menu")
        os.system('cls')
        Start_Manager.start()

    if count == 0:
        print("You have not saved any passwords yet")
        time.sleep(3)
        os.system('cls')
        Start_Manager.start()
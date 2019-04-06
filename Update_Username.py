import sqlite3
import time
import Start_Manager
import os

#                                                                                               #
# This abstraction allows the user to update a username in any account they have in the databse #
#                                                                                               #

def username():

    os.system('cls')

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
        print("{:25}   {:30}   {:81}".format(row[0], row[1], row[2]))

    print("\nWhich account are you updating?")
    time.sleep(1.5)
    username = input("\nType in the username or email of the account\n")

    new_username = input("\nWhat's your new username?\n")

    c.execute("SELECT * FROM PasswordManager")
    c.execute("UPDATE PasswordManager SET Username=? WHERE Username=?", (new_username, username))
    conn.commit()
    conn.close()

    print("\nUpdated username to " + new_username)
    time.sleep(1.5)
    os.system('cls')
    Start_Manager.start()
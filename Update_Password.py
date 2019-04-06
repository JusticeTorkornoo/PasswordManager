import sqlite3
import time
import random
import string
import Start_Manager
import os

#                                                                                              #
# This abstraction allows the user update a password for any account they have in the database #
#                                                                                              #

def password():

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
    answer = input("\nChoose a number from the options below\n1. Make your own password\n2. Generate a password\n\n")

    if "1" in answer:
        new_password = input("\nWhat's your new password?\n")

        c.execute("SELECT * FROM PasswordManager")
        c.execute("UPDATE PasswordManager SET Password=? WHERE Username=?", (new_password, username))

        #                                                                   #
        # "conn.commit()" will save the previous action in the database and #
        # "conn.close()" closes the database so no unwanted data enters the #
        # database on accident                                              #
        #                                                                   #
        
        conn.commit()
        conn.close()
        print("\nUpdated password")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()

    if "2" in answer:
        print("\nHow many characters do you want you password to have?\n")
        answer = input("It can be up to 81 characters\n")
        PassLen = int(answer)

        if PassLen > 81:
            print("\nThe password needs to be 81 characters and lower")
            time.sleep(3)
            restart()

        specialC = input("\nDo you want special characters like $ or & in your password?\n").lower()

        if specialC == "y" or specialC == "yes":
            passwordCharacters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()_+[]\;',./{}|:<>?*1234567890"
            Password =  "".join(random.sample(passwordCharacters,PassLen))

        if specialC == "n" or specialC == "no":
            passwordCharacters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            Password =  "".join(random.sample(passwordCharacters,PassLen))

        c.execute("SELECT * FROM PasswordManager")
        c.execute("UPDATE PasswordManager SET Password=? WHERE Username=?", (Password, username))

            #                                                                   #
            # "conn.commit()" will save the previous action in the database and #
            # "conn.close()" closes the database so no unwanted data enters the #
            # database on accident                                              #
            #                                                                   #

        conn.commit()
        conn.close()

        print("\nUpdated password")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()

def restart():
    password()
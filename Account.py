import sqlite3
import time
import random
import string
import os
import Start_Manager

#                                                                                #
# This abstraction controls what the user will do next depending on their answer #
#                                                                                #
def newAccount():
    Username = input("Whats the username or email for your account?\n")
    print()

    Website = input("What's the name of the webiste you are saving your login info for?\n").lower()
    print()

    answer = input("Choose a number from the options below\n1. Make your own password\n2. Generate a password\n\n")
#                                                                                                         #
# If the variable answer contains the string "my own", it will allow the user to enter their own password #
# after entering the website and username                                                                 #
#                                                                                                         #
    if answer == "1":

        Password = input("\nEnter your password\n")
        #                                                                                                    #
        # the variable "conn" was made so you dont have to type in "sqlite3.connect('PasswordManager.db')"   #
        # every time you wanted to connect to the database. The variable "c" was made to shorten the command #
        # connecting to the database even more when setting the cursor where you want to start entering data #
        # to the database                                                                                    #
        #                                                                                                    #

        conn = sqlite3.connect('PasswordManager.db')
        c = conn.cursor()

       #                                                                                                     #
       # c.execute('CREATE TABLE IF NOT EXISTS PasswordManager(Website TEXT, Username TEXT, Password TEXT)') #
       # will make a new table for the database if there isn't one already in the password manager folder    #
       #                                                                                                     #

        c.execute('CREATE TABLE IF NOT EXISTS PasswordManager(Website TEXT, Username TEXT, Password TEXT)')

        c.execute("INSERT INTO PasswordManager (Website, Username, Password) VALUES (?, ?, ?)",(Website, Username, Password))
        conn.commit()
        conn.close()

        print("\nYour credentials have been saved")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()

        #                                                                         #
        # If the variable answer contains the strings "make" "me" and "password", #
        # the password manager will make the password for the user                #
        # after entering the website and username                                 #
        #                                                                         #
        
    if answer == "2":
        print("\nHow many characters do you want you password to have?")
        answer = input("It can be up to 81 characters\n\n")
        PassLen = int(answer)

        specialC = input("\nDo you want special characters like $ or & in your password?\n")

        if specialC == "y" or specialC == "yes":
            passwordCharacters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ`!@#$%^&*()_+[]\;',./{}|:<>?*1234567890"

            #                                                                                 #
            # The join function takes a random character from the passwordCharacters varialbe #
            # and the length of the generated password will be PassLen                        #
            #                                                                                 #
             
            Password =  "".join(random.sample(passwordCharacters,PassLen))

        if specialC == "n" or specialC == "no":
            passwordCharacters= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
            Password =  "".join(random.sample(passwordCharacters,PassLen))

        conn = sqlite3.connect('PasswordManager.db')
        c = conn.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS PasswordManager(Website TEXT, Username TEXT, Password TEXT)')

        c.execute("INSERT INTO PasswordManager (Website, Username, Password) VALUES (?, ?, ?)",(Website, Username, Password))
        conn.commit()
        conn.close()

        print("\nYour credentials have been saved")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()
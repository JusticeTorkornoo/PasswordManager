import sqlite3
import time
import Delete_All
import Start_Manager
import os

#                                                                               #
# This abstraction controls whether only one account or all of them are deleted #
#                                                                               #

def deleteAccount():
    print("Do you want to delete one account or all accounts?")
    answer = input()
    print()

    if "one" in answer or "1" in answer:

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

        #                                                                                           #
        # "SELECT * FROM PasswordManager" means that SQlite will select all the data in the databse # 
        # The for loop is there to traverse through the whole database to print all the accounts in #
        # the database                                                                              #
        #                                                                                           #
        
        c.execute("SELECT * FROM PasswordManager")
        print("Website                Username               Password")
        print()
        for row in c.fetchall():
            print("{:20}   {:20}   {:81}".format(row[0], row[1], row[2]))

        print()
        print("Which account do you want to delete?")
        time.sleep(1.5)
        print()
        print("Type in the username of the account you want to delete")

        answer = input()

        c.execute("DELETE FROM PasswordManager WHERE Username=?", (answer,))

        #                                                                   #
        # "conn.commit()" will save the previous action in the database and #
        # "conn.close()" closes the database so no unwanted data enters the #
        # database on accident                                              #
        #                                                                   #
        
        conn.commit()
        conn.close()

        print()
        print(answer + " account deleted")
        time.sleep(1.5)
        os.system('cls')
        Start_Manager.start()

    if "all" in answer:
        os.system('cls')
        Delete_All.deleteAll()
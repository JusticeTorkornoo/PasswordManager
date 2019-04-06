import sqlite3
import time
import Start_Manager

#                                                                                         #
# This abstraction allows the user to be able to update any website thats on any of their #
# accounts in the database                                                                #
#                                                                                         #

def website():

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
    username = input("Type in the username of the account\n\n")
    print()

    new_website = input("What's the new website?\n").lower()

    c.execute("SELECT * FROM PasswordManager")
    c.execute("UPDATE PasswordManager SET Website=? WHERE Username=?", (new_website, username))

    #                                                                   #
    # "conn.commit()" will save the previous action in the database and #
    # "conn.close()" closes the database so no unwanted data enters the #
    # database on accident                                              #
    #                                                                   #
    
    conn.commit()
    conn.close()

    print("\nUpdated website to " + new_website)
    time.sleep(1.5)
    Start_Manager.start()
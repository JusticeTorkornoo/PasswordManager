import sqlite3
import os
import Start_Manager
import time

def search():
    os.system('cls')

    answer = input("Type the website of the accounts you want to search for\n")

    conn = sqlite3.connect('PasswordManager.db')
    c = conn.cursor()

    sql = "SELECT * FROM PasswordManager WHERE Website=?"

    print("\nWebsite                     Username                         Password")
    print()
    for row in c.execute(sql, (answer,)):
        print("{:25}   {:30}   {:81}".format(row[0], row[1], row[2]))

    time.sleep(2.5)
    input("\nPress ENTER to go back to main menu")
    os.system('cls')
    Start_Manager.start()
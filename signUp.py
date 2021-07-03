from sqlite3 import Error
from tkinter import *
import sqlite3
import hashlib

import HomePage


def check_table_exists():
    db_file = 'sqliteDB/morseCode.db'

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    query = "CREATE TABLE IF NOT EXISTS userInfo " \
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
            "username STRING, " \
            "password STRING);"

    conn.execute(query)


def hash_password(raw_password):
    encoded = raw_password.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()


def check_db_for_user(username, hashed_pw):
    db_file = 'sqliteDB/morseCode.db'

    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    cursor = conn.cursor()

    cursor.execute("SELECT rowid FROM userInfo WHERE username = ?", (username,))

    data = cursor.fetchall()

    if len(data) == 0:
        print('There is no user named %s' % username)
    else:
        return True
        # query = "CREATE TABLE IF NOT EXISTS userInfo " \
        #         "(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
        #         "username STRING, " \
        #         "password STRING);"
        #
        # cursor.execute(query)

    return True


def check_user_exists(username, raw_password):
    # check if table exist
    check_table_exists()

    hashed_pw = hash_password(raw_password)

    check_db_for_user(username, hashed_pw)

    return False


def home_page(root, username, raw_password):
    print(username + " | " + raw_password)

    # check if user exists
    if check_user_exists(username, raw_password):
        root.destroy()
        HomePage.home_page() # pass the username as an argument for use later


class sign_up:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x300')
        self.root.title("Registration Form")
        label_0 = Label(self.root, text="Registration form", width=20, font=("bold", 20))
        label_0.place(x=90, y=53)
        label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=240, y=130)
        label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        label_2.place(x=80, y=180)
        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=240, y=180)

        Button(self.root,
               text='Submit',
               width=20,
               bg='brown',
               fg='white',
               command=lambda: home_page(self.root,
                                         self.entry_1.get(),
                                         self.entry_2.get())).place(x=180, y=230)
        # Button(self.root, text='Sign in', width=20, bg='brown', fg='white', command=lambda: home_page(self.root)).place(x=180, y=380)

        self.root.mainloop()
        print("registration form  successfully created...")


if __name__ == "__main__":
    root1 = sign_up()

from sqlite3 import Error
from tkinter import *
import sqlite3
import hashlib

import HomePage
import Login


def check_table_exists():
    print("In check_table_exists")

    db_file = 'sqliteDB/morseCode.db'

    try:
        conn = sqlite3.connect(db_file)

        query = "CREATE TABLE IF NOT EXISTS userInfo " \
                "(id INTEGER PRIMARY KEY AUTOINCREMENT, " \
                "username STRING, " \
                "password STRING);"

        conn.execute(query)

    except Error as e:
        print(e)


def hash_password(raw_password):
    print("In hash_password")

    encoded = raw_password.encode()
    result = hashlib.sha256(encoded)
    return result.hexdigest()


class sign_up:

    def check_db_for_user(self, username, hashed_pw):
        print("In check_db_for_user")
        db_file = 'sqliteDB/morseCode.db'

        try:
            conn = sqlite3.connect(db_file)

            cursor = conn.cursor()

            cursor.execute("SELECT rowid, username, password FROM userInfo WHERE username = ?", (username,))

            data = cursor.fetchall()

            print(data)

            if len(data) == 0:
                # the user doesnt exist

                # create new user
                cursor.execute("INSERT INTO userInfo(username, password) VALUES (?, ?)",
                               (username, hashed_pw))

                cursor.execute("SELECT rowid, username, password FROM userInfo WHERE username = ?", (username,))

                data = cursor.fetchall()

                print("2", data)
                cursor.close()

                conn.commit()
                return True

            else:
                self.warning_1['text'] = 'User already exists!'

                return False

        except Error as e:
            print(e)

        return False

    def check_user_exists(self, username, raw_password):
        # check if table exist
        check_table_exists()

        hashed_pw = hash_password(raw_password)

        return self.check_db_for_user(username, hashed_pw)

    def home_page(self, root, username, raw_password):
        if not username.strip():
            self.warning_1['text'] = 'Username cannot be empty!'
            return

        if not raw_password.strip():
            self.warning_1['text'] = 'Password cannot be empty!'
            return

        print(username + " | " + raw_password)

        # check if user exists
        if self.check_user_exists(username, raw_password):
            root.destroy()
            HomePage.home_page()  # pass the username as an argument for use later

    def login_instead(self):
        self.root.destroy()
        Login.login()

    def show(self):
        self.entry_2.configure(show='')
        self.check.configure(command=self.hide, text='hide password')

    def hide(self):
        self.entry_2.configure(show='*')
        self.check.configure(command=self.show, text='show password')

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x300')
        self.root.title("No-re-morse")

        self.label_0 = Label(self.root, text="Sign up", width=20, font=("bold", 20))
        self.label_0.place(x=90, y=53)

        self.warning_1 = Label(self.root, text="", width=20, font=("bold", 10))
        self.warning_1.config(fg="red")
        self.warning_1.place(x=170, y=100)
        self.warning_1.configure(anchor="center")

        self.label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        self.label_1.place(x=80, y=130)

        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=240, y=130)

        self.label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        self.label_2.place(x=80, y=180)

        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=240, y=180)

        self.check = Checkbutton(self.root, text='show password',
                                 command=self.show)
        self.check.place(x=240, y=200)

        self.submitBtn = Button(self.root,
                               text='Submit',
                               width=9,
                               bg='brown',
                               fg='white',
                               command=lambda: self.home_page(self.root,
                                                              self.entry_1.get(),
                                                              self.entry_2.get())).place(x=280, y=250)
        self.loginButton = Button(self.root,
                                   text='Log in',
                                   width=9,
                                   bg='brown',
                                   fg='white',
                                   command=lambda: self.login_instead()).place(x=130, y=250)

        self.root.mainloop()
        print("registration form  successfully created...")


if __name__ == "__main__":
    root1 = sign_up()

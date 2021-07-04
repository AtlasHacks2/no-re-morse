from sqlite3 import Error
from tkinter import *
import sqlite3
import hashlib

import HomePage
import signUp


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


class login:

    def check_db_for_user(self, username, hashed_pw):
        print("In check_db_for_user")
        db_file = 'sqliteDB/morseCode.db'

        try:
            conn = sqlite3.connect(db_file)

            cursor = conn.cursor()

            cursor.execute("SELECT rowid, username, password FROM userInfo WHERE username = ?", (username,))

            data = cursor.fetchall()

            if len(data) == 0:
                self.warning_1['text'] = 'User not found!'
                # the user doesnt exist

                return False

            else:
                print(data[0][2])
                if data[0][2] == hashed_pw:
                    return True
                else:
                    self.warning_1['text'] = 'Incorrect password!'

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
            HomePage.home_page(username)  # pass the username as an argument for use later

    def show(self):
        self.entry_2.configure(show='')
        self.check.configure(command=self.hide, text='hide password')

    def hide(self):
        self.entry_2.configure(show='*')
        self.check.configure(command=self.show, text='show password')

    def sign_up_insetead(self):
        self.root.destroy()
        signUp.sign_up()

    def __init__(self):
        self.root = Tk()
        self.root.geometry('920x570')
        self.root.title("No-re-morse")
        self.root.iconbitmap('FireAnts_logo.ico')
        # Define image
        bg = PhotoImage(file="junk/Sign_upAndLog_in.png")

        # Create a canvas
        my_canvas = Canvas(self.root, width=500, height=300)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor="nw")

        self.label_0 = Label(self.root, text="Login", width=20, font=("bold", 20))
        self.label_0.place(x=460, y=100)

        self.warning_1 = Label(self.root, text="", width=20, font=("bold", 10))
        self.warning_1.config(fg="red")
        self.warning_1.place(x=500, y=150)
        self.warning_1.configure(anchor="center")

        self.label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        #self.label_1.place(x=0, y=130)
        my_canvas.create_window(600, 250, window=self.label_1)

        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=700, y=240)


        self.label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        #self.label_2.place(x=80, y=180)
        my_canvas.create_window(600, 300, window=self.label_2)

        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=700, y=290)
        #my_canvas.create_window(700, 290, window=self.entry_2)

        self.check = Checkbutton(self.root, text='show password',
                            command=self.show)
        #self.check.place(x=240, y=200)
        my_canvas.create_window(800, 340, window=self.check)
        self.submit= Button(self.root,
               text='Submit',
               width=9,
               bg='#BAC1FF',
               fg='black',
               command=lambda: self.home_page(self.root,
                                         self.entry_1.get(),
                                         self.entry_2.get()))

        my_canvas.create_window(750, 425, window=self.submit)

        self.sign_up = Button(self.root,
               text='Sign up',
               width=9,
               bg='#BAC1FF',
               fg='black',
               command=lambda: self.sign_up_insetead())
        my_canvas.create_window(590, 420, window=self.sign_up)


        self.root.mainloop()
        print("registration form  successfully created...")


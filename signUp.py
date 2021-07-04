from sqlite3 import Error
from tkinter import *
import sqlite3
import hashlib
from tkinter import font

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
            HomePage.home_page(username)  # pass the username as an argument for use later

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
        # Creating a Font object of "TkDefaultFont"
        # self.defaultFont = font.nametofont("TkDefaultFont")
        #
        # # Overriding default-font with custom settings
        # # i.e changing font-family, size and weight
        # self.defaultFont.configure(family="Comic Sans MS",
        #                            size=19)
        #my_canvas.create_text(460, 100,text="Sign up", width=40, font=("bold", 20), fill="white")
        #my_canvas.create_text(170, 100, text="", width=20, font=("bold", 10), fill="red",anchor = 'center')

        self.label_0 = Label(self.root, text="Sign up", width=20, font=("bold", 20))
        self.label_0.place(x=460, y=100)
        self.warning_1 = Label(self.root, text="", width=20, font=("bold", 10))
        self.warning_1.config(fg="red")
        self.warning_1.place(x=500, y=150)
        self.warning_1.configure(anchor="center")
        #my_canvas.create_window(500, 150, window = self.warning_1)

        self.label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        #self.label_1.place(x=80, y=130)
        my_canvas.create_window(600, 250, window=self.label_1)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=700, y=240)

        self.label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        #self.label_2.place(x=700, y=300)
        my_canvas.create_window(600, 300, window=self.label_2)
        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=700, y=290)

        self.check = Checkbutton(self.root, text='show password',
                                 command=self.show)
        self.check.place(x=800, y=340)
        my_canvas.create_window(800, 340, window=self.check)
        self.submitBtn = Button(self.root,
                               text='Submit',
                               width=9,
                               bg='#BAC1FF',
                               fg='black',
                               command=lambda: self.home_page(self.root,
                                                              self.entry_1.get(),
                                                              self.entry_2.get()))
        self.submitBtn.pack(pady=20)
        my_canvas.create_window(700, 410, anchor="nw", window=self.submitBtn)
        self.loginButton = Button(self.root,
                                   text='Log in',
                                   width=9,
                                   bg='#BAC1FF',
                                   fg='black',
                                   command=lambda: self.login_instead())
        my_canvas.create_window(600, 420, window=self.loginButton)

        self.root.mainloop()
        print("registration form  successfully created...")


if __name__ == "__main__":
    root1 = sign_up()

from tkinter import *
import sqlite3
import HomePage


def check_password(username, raw_password):
    # conn = sqlite3.connect('sql/testNyoomba.db')
    return False


def home_page(root, username, raw_password):
    # check if user exists
    if check_password(username, raw_password):
        var = True



    root.destroy()
    HomePage.home_page()


class sign_up:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Registration Form")
        label_0 = Label(self.root, text="Registration form", width=20, font=("bold", 20))
        label_0.place(x=90, y=53)
        label_1 = Label(self.root, text="Username", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=240, y=130)
        label_2 = Label(self.root, text="Password", width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        self.entry_2 = Entry(self.root, show="*")
        self.entry_2.place(x=240, y=180)

        # label_3 = Label(self.root, text="Gender", width=20, font=("bold", 10))
        # label_3.place(x=70, y=230)
        # var = IntVar()
        # Radiobutton(self.root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
        # Radiobutton(self.root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
        # label_4 = Label(self.root, text="Age:", width=20, font=("bold", 10))
        # label_4.place(x=70, y=280)
        # self.entry_2 = Entry(self.root)
        # self.entry_2.place(x=240, y=280)

        Button(self.root, text='Submit', width=20, bg='brown', fg='white', command=lambda: home_page(self.root, self.entry_1.get(), self.entry_2.get())).place(x=180, y=380)
        # Button(self.root, text='Sign in', width=20, bg='brown', fg='white', command=lambda: home_page(self.root)).place(x=180, y=380)

        self.root.mainloop()
        print("registration form  successfully created...")

# ERROR : __init__() should return None, not 'Tk'

if __name__ == "__main__":
    root1 = sign_up()

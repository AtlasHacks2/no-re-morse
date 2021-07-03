from tkinter import *

import HomePage


class LevelOne:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Play")

        self.label_1 = Label(self.home, text=HomePage.home_page.name, width=20, font=("bold", 10))
        self.label_1.place(x=10, y=10)
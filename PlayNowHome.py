from tkinter import *

import Level1
import Level2
import Level3
import Level4
import Level10
import HomePage


def L1(root):
    root.destroy()
    Level1.LevelOne()


def L2(root):
    root.destroy()
    Level2.LevelTwo()


def L3(root):
    root.destroy()
    Level3.LevelThree()


def L4(root):
    root.destroy()
    Level4.LevelFour()


def L10(root):
    root.destroy()
    Level10.LevelTen()


def Home(root):
    root.destroy()
    HomePage.home_page()


class playnow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title("Play")
        Button(self.root, text='Level 1', width=20, bg='brown', fg='white', command=lambda: L1(self.root)).place(x=100,
                                                                                                                 y=100)
        Button(self.root, text='Level 2', width=20, bg='brown', fg='white', command=lambda: L2(self.root)).place(x=300,
                                                                                                                 y=100)
        Button(self.root, text='Level 3', width=20, bg='brown', fg='white', command=lambda: L3(self.root)).place(x=500,
                                                                                                                 y=100)
        Button(self.root, text='Level 4', width=20, bg='brown', fg='white', command=lambda: L4(self.root)).place(x=100,
                                                                                                                 y=300)
        Button(self.root, text='Level 5', width=20, bg='brown', fg='white').place(x=300, y=300)
        Button(self.root, text='Level 6', width=20, bg='brown', fg='white').place(x=500, y=300)
        Button(self.root, text='Level 7', width=20, bg='brown', fg='white').place(x=100, y=500)
        Button(self.root, text='Level 8', width=20, bg='brown', fg='white').place(x=300, y=500)
        Button(self.root, text='Level 9', width=20, bg='brown', fg='white').place(x=500, y=500)
        Button(self.root, text='Level 10', width=20, bg='brown', fg='white', command=lambda: L10(self.root)).place(
            x=100, y=700)

        Button(self.root, text='Home', width=20, bg='brown', fg='white', command=lambda: Home(self.root)).place(x=40,
                                                                                                                y=20)

        label_1 = Label(self.root, text=HomePage.home_page.name, width=20, font=("bold", 10))
        label_1.place(x=600, y=10)
        self.root.mainloop()

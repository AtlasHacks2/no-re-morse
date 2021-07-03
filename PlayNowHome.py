from tkinter import *
import Level1
import Level2
import Level3
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

def Home(root):
    root.destroy()
    HomePage.home_page()

class playnow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title("Play")
        Button(self.root, text='Level 1', width=20,bg='brown', fg='white',command=lambda: L1(self.root)).place(x=180, y=20)
        Button(self.root, text='Level 2', width=20, bg='brown', fg='white',command=lambda: L2(self.root)).place(x=180, y=100)
        Button(self.root, text='Level 3', width=20, bg='brown', fg='white', command=lambda: L3(self.root)).place(x=180, y=180)
        Button(self.root, text='Level 4', width=20, bg='brown', fg='white').place(x=180, y=260)
        Button(self.root, text='Level 5', width=20, bg='brown', fg='white').place(x=180, y=340)
        Button(self.root, text='Level 6', width=20, bg='brown', fg='white').place(x=180, y=420)
        Button(self.root, text='Level 7', width=20, bg='brown', fg='white').place(x=180, y=500)
        Button(self.root, text='Level 8', width=20, bg='brown', fg='white').place(x=180, y=580)
        Button(self.root, text='Level 9', width=20, bg='brown', fg='white').place(x=180, y=640)
        Button(self.root, text='Level 10', width=20, bg='brown', fg='white').place(x=180, y=720)
        Button(self.root, text='Home', width=20, bg='brown', fg='white', command=lambda: Home(self.root)).place(x=40,
                                                                                                                y=20)
        self.root.mainloop()
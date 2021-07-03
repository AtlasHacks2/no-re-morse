from tkinter import *
import Tutorial
import PlayNowHome


def learn(root):
    root.destroy()
    Tutorial.tutorial()


def Play(root):
    root.destroy()
    PlayNowHome.playnow()


class home_page:
    name = ""

    def __init__(self, username):

        name = username
        self.home = Tk()
        self.home.title('Home Page')
        self.home.geometry("500x300")
        # Add image file
        #bg = PhotoImage(file="Your_img.png")

        # Show image using label
        #background = Label(self.home, image=bg)
        #background.place(x=0, y=0)


        learn_button = Button(self.home, text="Learn now", fg='blue', command=lambda: learn(self.home)).place(x=80, y=100)
        play = Button(self.home, text="Play Now", fg='blue', command=lambda: Play(self.home))
        play.place(x=80, y=50)
        suggested = Button(self.home, text="Suggested to know", fg='blue')
        suggested.place(x=80, y=150)

        label_1 = Label(self.home, text=username, width=20, font=("bold", 10))
        label_1.place(x=10, y=10)

        self.home.mainloop()

from tkinter import *
import HomePage
def Home(root):
    root.destroy()
    HomePage.home_page(HomePage.home_page.name)

class Story:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('400x480'
                           '')
        self.root.title("Play")

        self.root.iconbitmap('FireAnts_logo.ico')
        # Define image
        bg = PhotoImage(file="junk/Sign_upAndLog_in.png")

        # Create a canvas
        my_canvas = Canvas(self.root, width=710, height=580)
        my_canvas.pack(fill="both", expand=True)
        # Set image in canvas
        my_canvas.create_image(0, 0, image=bg, anchor="nw")
        msg = Message(self.root, text="Hello ! Fellow Captain . You are stuck on a spaceship and are recieving signals which sound like Morse code . You have to figure out the signal ‘s meaning before time runs out!!! But dont worry , we have manuals and much more to help you train ",font = "200").place(x=100,y=100)
        msg2 = Message(self.root,text="So are you ready to start your journey ???",font="200").place(x = 100,y= 300)
        Button(self.root, text='Home', width=20, bg='#BAC1FF', fg='black', command=lambda: Home(self.root)).place(x=50,y=50)
        self.root.mainloop()


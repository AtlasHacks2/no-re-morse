from tkinter import *
import webbrowser


def openweb(url):
    webbrowser.open(url,new=1)

def hyper(url):
    if __name__ == "__main__":
        import webbrowser
        try:
            from Tkinter import Tk, Frame
        except ImportError:
            from tkinter import Tk, Frame
        def callback():
            webbrowser.open_new(r"https://www.youtube.com/watch?v=D8tPkb98Fkk")
        root = Tk()
        frame = Frame(root, bg="white")
        frame.pack(expand=True, fill="both")
        link = tutorial(frame, text="Google Hyperlink", action=callback)
        link.pack(padx=10, pady=10)

class tutorial:
    def __init__(self):
        self.learn = Tk()
        self.learn.title('learnPage')
        self.learn.geometry("300x200+10+20")

        # Add image file
        #bg = PhotoImage(file="Your_img.png")
        # Show image using label
        #background = Label(self.learn, image=bg)
        #background.place(x=0, y=0)

        button1 = Button(self.learn, text="Learn now", fg='blue')
        button1.place(x=80, y=100)
       # link = Label(self.learn, text="https://www.youtube.com/watch?v=D8tPkb98Fkk", fg="blue", cursor="hand2",)
        #link.pack()
        #link.bind("<button1>", lambda event: webbrowser.open(link.cget("text")))
        self.learn.mainloop()



from tkinter import *
import webbrowser
import HomePage

# CALL BACK FUNCTION
def callback(url):
    webbrowser.open(url,new=1)


def Home(root):
    root.destroy()
    HomePage.home_page(HomePage.home_page.name)

class tutorial:
    def __init__(self):
        #CREATES INSTANCE OF TKINTER FRAM
        self.learn = Tk()
        self.learn.title('learnPage')
        self.learn.geometry("")
        Button(self.learn, text='Home', width=20, bg='brown', fg='white', command=lambda: Home(self.learn)).place(x=40,
                                                                                                                y=20)
        # CREATES LABEL FOR HYPERLINK
        link1 = Label(self.learn, text="LEARN MORSE CODE from a MEMORY CHAMP (in 15 minutes)", font=('Maiden Oranged', 10), fg="blue", cursor="hand2",bg="grey")
        link1.pack()
        link1.bind("<Button-1>", lambda e:callback("https://www.youtube.com/watch?v=D8tPkb98Fkk"))
        # CREATES LABEL FOR HYPERLINK
        link1 = Label(self.learn, text="Morse Code Sound Effects(2 minute video)",font=('Maiden Orange', 10), fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=GFUHBV8Yn8E"))
        # CREATES LABEL FOR HYPERLINK
        link1 = Label(self.learn, text="How I learned MORSE CODE IN 10 MINUTES | learn fast(3 minute video)", font=('Maiden Orange', 10), fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://www.youtube.com/watch?v=QAd2Weqz1fk"))
        # CREATES LABEL FOR HYPERLINK
        link1 = Label(self.learn, text="Morse Code Tutorial With Good Explaining.(14 minute video)",
                      font=('Helvetica bold', 15), fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://youtu.be/FuCKs6mWYwA"))
        # CREATES LABEL FOR HYPERLINK
        link1 = Label(self.learn, text="The Morse Code(7 minute video)",
                      font=('Helvetica bold', 15), fg="blue", cursor="hand2")
        link1.pack()
        link1.bind("<Button-1>", lambda e: callback("https://youtu.be/Z-kZHXBqj4A"))




        self.learn.mainloop()



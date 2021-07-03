
from tkinter import *
import re
from random import sample
import random
import HomePage
import Constants

def Home(root):
    root.destroy()
    HomePage.home_page(HomePage.home_page)

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

def eng_to_morse_code(message):
    my_cipher = ''
    for myletter in message:
        if myletter != ' ':
            my_cipher += Constants.MORSE_CODE_DICT[myletter] + ' '
        else:
            my_cipher += ' '
        return my_cipher


class LevelTen:
    def go_home(self):
        self.root.destroy()
        HomePage.home_page(HomePage.home_page.name)

    def check(input, text, warning_1):
        if (input).equals(eng_to_morse_code(text)):
            warning_1['text'] = 'CORRECT ANSWER'
        else:
            warning_1['text'] = 'WRONG ANSWER , TRY AGAIN!!'

    def __init__(self):
        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Play")
        self.warning_1 = Label(self.root, text="", width=20, font=("bold", 10))
        self.warning_1.config(fg="red")
        self.warning_1.place(x=170, y=100)
        self.warning_1.configure(anchor="center")



        # sentences = []
        # for i in range(23):
        #     with open('AlphaHacksSample.txt'.format(i)) as f:
        #         sentences += re.findall(r".*?[\.\!\?]+", f.read())
        #
        # selected = sample(sentences, 1000)
        # with open('out.txt', 'w') as f:
        #     f.write(''.join(selected))

        # s = open("AlphaHacksSampleText.txt", "r")
        # m = s.readlines()
        # l = []
        # for i in range(0, len(m) - 1):
        #     x = m[i]
        #     z = len(x)
        #     a = x[:z - 1]
        #     l.append(a)
        # l.append(m[i + 1])
        # o = random.choice(l)
        # print(o)
        # s.close()

        sentence = random_line('AlphaHacksSampleText.txt')
        self.labelQ = Label(self.root, text="Enter the morse code for the following sentence", width=40, font=("bold", 10))
        self.labelQ.place(x=90, y=33)
        self.label_0 = Label(self.root, text=sentence, width=40, font=("bold", 10))
        self.label_0.place(x=100, y=53)
        self.labelA= Label(self.root, text="Enter Answer", width=30, font=("bold", 10))
        self.labelA.place(x=100, y=90)
        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=160, y=90)
        self.root.mainloop()
        self.submitBtn = Button(self.root,text='Submit',width=9,bg='brown',fg='white',command=lambda: self.check(self.root,self.entry_1.get(),self.warning_1)).place(x=280, y=250)

from tkinter import *
import random

import HomePage
import Constants


class LevelOne:
    def get_first_letter(self, num):
        return Constants.ALPHABETICAL_STRING[num]

    def check_num(self, first_letter, second_letter):
        self.entry_1.delete(0, 'end')

        if self.score == Constants.ALPHABET:
            return

        # check if the strings are equal
        if first_letter == second_letter.capitalize():
            # remove current letter from list
            self.random_26.pop(0)
            print(self.random_26)

            # if the score is == 26, display the next button
            if len(self.random_26) == 0:
                # show the list
                self.score = Constants.ALPHABET
                self.score_label['text'] = self.score
                self.error_msg['text'] = "You did it!"
                self.error_msg.config(fg="blue")

            else:
                # change the label and increment the score
                self.first_letter = self.get_first_letter(self.random_26[0])
                print(self.first_letter)

                self.first_morse = self.get_first_morse(self.first_letter)

                self.morse_2['text'] = self.first_morse

                self.error_msg['text'] = ''

                self.score += 1

                self.score_label['text'] = self.score


        else:
            # else if not equal, then change label to say wrong answer
            if self.error_msg['text'] == 'Wrong answer!':
                self.error_msg['text'] = 'Nope! Try Again!'
            else:
                self.error_msg['text'] = 'Wrong answer!'


    def get_first_morse(self, first_letter):
        return Constants.MORSE_CODE_DICT.get(first_letter)

    def __init__(self):
        self.score = 0

        self.random_26 = list(range(0, Constants.ALPHABET))
        random.shuffle(self.random_26)
        print(self.random_26)

        # get first letter
        print(self.random_26[0])
        self.first_letter = self.get_first_letter(self.random_26[0])
        print(self.first_letter)

        self.first_morse = self.get_first_morse(self.first_letter)
        print(self.first_morse)


        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Identify the letter")

        self.name = Label(self.root, text=HomePage.home_page.name, width=20, font=("bold", 10))
        self.name.place(x=50, y=30)

        self.score_label1 = Label(self.root, text="Score", width=10, font=("bold", 10))
        self.score_label1.place(x=260, y=30)

        self.score_label = Label(self.root, text=self.score, width=5, font=("bold", 10))
        self.score_label.place(x=320, y=30)

        self.morse_1 = Label(self.root, text="Morse Code:", width=20, font=("bold", 10))
        self.morse_1.place(x=82, y=145)

        self.morse_2 = Label(self.root, text=self.first_morse, width=10, font=("bold", 30))
        self.morse_2.place(x=200, y=120)

        self.ans_1 = Label(self.root, text="What letter is this?", width=20, font=("bold", 10))
        self.ans_1.place(x=100, y=190)

        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=250, y=190)

        self.error_msg = Label(self.root, text="", width=20, font=("bold", 10))
        self.error_msg.place(x=150, y=90)
        self.error_msg.config(fg="red")
        self.error_msg.configure(anchor="center")

        self.submit = Button(self.root,
               text='Submit',
               width=9,
               bg='brown',
               fg='white',
               command=lambda: self.check_num(self.first_letter,
                                              self.entry_1.get())).place(x=280, y=250)

        self.back = Button(self.root,
               text='Back',
               width=9,
               bg='blue',
               fg='white',
               command=lambda: self.go_home()).place(x=140, y=250)

    def go_home(self):
        self.root.destroy()
        HomePage.home_page(HomePage.home_page.name)
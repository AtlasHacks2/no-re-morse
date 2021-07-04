import time
from tkinter import *
import random

import HomePage
import Constants
import AudioPlayer
import SoundGeneration


def get_first_letter(num):
    return Constants.NON_ALPHABET_STRING[num]


def get_first_morse(first_letter):
    return Constants.MORSE_CODE_DICT.get(first_letter)


def play_sound():
    AudioPlayer.start_music("morseSound.wav", 2)


class LevelFour:


    def go_home(self):
        self.root.destroy()
        HomePage.home_page(HomePage.home_page.name)

    def check_num(self, first_letter, second_letter):
        self.entry_1.delete(0, 'end')

        if self.score == Constants.NON_ALPHABET:
            return

        # check if the strings are equal
        if first_letter == second_letter.capitalize():
            # remove current letter from list
            self.random_17.pop(0)
            print(self.random_17)

            # if the score is == 26, display the next button
            if len(self.random_17) == 0:
                # show the list
                self.score = Constants.ALPHABET
                self.score_label['text'] = self.score
                self.error_msg['text'] = "You did it!"
                self.error_msg.config(fg="blue")

            else:
                # self.play_clear_sound()
                # change the label and increment the score
                self.set_new_round()

                # play once

                self.error_msg['text'] = ''

                self.score += 1

                self.score_label['text'] = self.score

        else:
            # else if not equal, then change label to say wrong answer
            if self.error_msg['text'] == 'Wrong answer!':
                self.error_msg['text'] = 'Nope! Try Again!'
            else:
                self.error_msg['text'] = 'Wrong answer!'

    def set_new_round(self):

        # get first letter
        print(self.random_17[0])
        self.first_letter = get_first_letter(self.random_17[0])
        print(self.first_letter)

        self.first_morse = get_first_morse(self.first_letter)
        print(self.first_morse)

        SoundGeneration.clear_old_file()
        SoundGeneration.generate_wav(SoundGeneration.generate_morse_array(self.first_letter))

    def __init__(self):
        self.score = 0

        self.random_17 = list(range(0, Constants.NON_ALPHABET))
        random.shuffle(self.random_17)
        print(self.random_17)

        self.set_new_round()

        self.root = Tk()
        self.root.geometry('500x500')
        self.root.title("Identify the character")

        self.root.iconbitmap('FireAnts_logo.ico')

        self.name = Label(self.root, text=HomePage.home_page.name, width=20, font=("bold", 10))
        self.name.place(x=50, y=30)

        self.score_label1 = Label(self.root, text="Score", width=10, font=("bold", 10))
        self.score_label1.place(x=260, y=30)

        self.score_label = Label(self.root, text=self.score, width=5, font=("bold", 10))
        self.score_label.place(x=320, y=30)

        self.morse_1 = Label(self.root, text="Press play to hear the sound!", width=30, font=("bold", 10))
        self.morse_1.place(x=120, y=100)

        self.ans_1 = Label(self.root, text="What character is this?", width=20, font=("bold", 10))
        self.ans_1.place(x=90, y=190)

        self.entry_1 = Entry(self.root)
        self.entry_1.place(x=260, y=190)

        self.error_msg = Label(self.root, text="", width=20, font=("bold", 10))
        self.error_msg.place(x=150, y=75)
        self.error_msg.config(fg="red")
        self.error_msg.configure(anchor="center")

        self.submit = Button(self.root,
                             text='Submit',
                             width=9,
                             bg='brown',
                             fg='white',
                             command=lambda: self.check_num(self.first_letter,
                                                            self.entry_1.get())).place(x=280, y=250)

        self.play = Button(self.root,
                           text='Play',
                           width=9,
                           bg='brown',
                           fg='white',
                           command=lambda: play_sound())
        self.play.place(x=210, y=145)

        self.back = Button(self.root,
                           text='Back',
                           width=9,
                           bg='blue',
                           fg='white',
                           command=lambda: self.go_home()).place(x=140, y=250)

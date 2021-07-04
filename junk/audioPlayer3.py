import time
from threading import Thread
from pygame import mixer


def play_music():
    # Starting the mixer
    mixer.init()

    # Loading the song
    mixer.music.load("sos.wav")

    # Setting the volume
    mixer.music.set_volume(1)

    # Start playing the song
    mixer.music.play(loops=1)


def stop_music():
    time.sleep(1)
    mixer.music.stop()
    music_thread.join()


# Play Music on Separate Thread (in background)
music_thread = Thread(target=play_music)

stop_music_thread = Thread(target=stop_music)

music_thread.start()

print("done")

stop_music_thread.start()
stop_music_thread.join()

# print("Does playsound block the main thread?")
# user_input = input("What is your guess?: ")
# print("You guessed: " + user_input)
#
# print("Dasdfthread?")
# user_input = input("Wasfess?: ")
# print("You guessed: " + user_input)

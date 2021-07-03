from pygame import mixer

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("newSound.wav")

# Setting the volume
mixer.music.set_volume(2)

# Start playing the song
mixer.music.play()

# need the program to continue otherwise it ends
while True:
    pass

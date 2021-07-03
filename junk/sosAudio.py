import Constants
import os
import wave


if os.path.exists("newSound.wav"):
  os.remove("newSound.wav")
else:
  print("The file does not exist")

message = "12-+@4adsv3rvq23t"

dot = "../soundFiles/dot.wav"
dash = "../soundFiles/dash4.wav"
space = "../soundFiles/space.wav"

morseArray = []


# Iterate over the string
for letter in message:
    caps_letter = letter.capitalize()
    if caps_letter.isspace():
        morseArray.append(space)
        morseArray.append(space)
    elif caps_letter in Constants.MORSE_CODE_DICT:
        morse_string = Constants.MORSE_CODE_DICT.get(caps_letter)
        print(morse_string)
        for char_morse in morse_string:

            if char_morse == ".":
                morseArray.append(dot)

            if char_morse == "-":
                if (len(morseArray) != 0) and (morseArray[-1] == dot):
                    morseArray.append(space)
                morseArray.append(dash)

print(morseArray)

outfile = "newSound.wav"

data = []
for infile in morseArray:
    w = wave.open(infile, 'rb')
    data.append([w.getparams(), w.readframes(w.getnframes())])
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()


import wave

dot = "../soundFiles/dot2.wav"
dash = "../soundFiles/dash2.wav"
space = "../soundFiles/space.wav"
infiles = [dot, dot, dot, space, dash, dash, dash, dot, dot, dot]

# infiles = ["../soundFiles/dot2.wav", "../soundFiles/dash2.wav", "../soundFiles/dot2.wav"]
outfile = "sounds9.wav"

data = []
for infile in infiles:
    w = wave.open(infile, 'rb')
    data.append([w.getparams(), w.readframes(w.getnframes())])
    w.close()

output = wave.open(outfile, 'wb')
output.setparams(data[0][0])
for i in range(len(data)):
    output.writeframes(data[i][1])
output.close()
from pydub import AudioSegment
from pydub.utils import make_chunks

##bluesfile 30s
audio = AudioSegment.from_file("../soundFiles/Powerup.wav", "wav")

size = 1000 ##The milliseconds of cutting

chunks = make_chunks(audio, size) ##Cut the file into 10s pieces

for i, chunk in enumerate(chunks):
         ##Enumeration, i is the index, chunk is the cut file
    chunk_name = "bulues{0}.wav".format(i)
    print(chunk_name)
         ##save document
    chunk.export(chunk_name, format="wav")

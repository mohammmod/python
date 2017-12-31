from gtts import gTTS
import os
import sys

name = sys.argv[1:4]
name = " ".join(name)
voice = gTTS(text='hello'+name, lang='en')
voice.save("dude.mp3")
os.system("mpg321 dude.mp3")

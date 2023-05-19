import speech_recognition as sr
import os
from playsound import playsound
import time
from search import searchWEB

import wikipedia
import random
import getpass
from pathlib import Path

from op import openAPP

username = getpass.getuser()

wiki_required = False


statusFile = open("status", "w")
statusFile.write("1")
statusFile.close()



def chooseResponse():
    if "what is your name" in text or "who are you":
        random_int = random.randint(1, 3)
        if random_int == 1:
            playsound("/home/"+username+"/ketta/data/audio-responses/name_1.wav")
        if random_int == 2:
            playsound("/home/"+username+"/ketta/data/audio-responses/name_2.wav")
        if random_int == 3:
            playsound("/home/"+username+"/ketta/data/audio-responses/name_3.wav")

    if "hello" in text or "hi" in text:
        random_int = random.randint(1, 3)
        print("Random integer : "+random_int)
        if random_int == 1:
            playsound("/home/"+username+"/ketta/data/audio-responses/hello_1.wav")
        if random_int == 2:
            playsound("/home/"+username+"/ketta/data/audio-responses/hello_2.wav")
        if random_int == 3:
            playsound("/home/"+username+"/ketta/data/audio-responses/hello_3.wav")

def open(appname):
    openAPP(appname)

def main():
    try:
        r = sr.Recognizer()
        data = sr.AudioFile("r1.wav")
        with data as source:
            audio = r.record(source)
            text = r.recognize_google(audio, language="en-IN")
            print(text)
            text = text.lower()

        if "open" in text:
            path = Path("/home/"+username+"/ketta/data/pyth.opt")
            text = text.replace("open", "")
            open(text.lower())


        else:
            print("no useful commands found")
            print("searching internet")
            searchWEB(text)

    except sr.UnknownValueError:
        print("no speech")


    print("recognition done")

    time.sleep(1)

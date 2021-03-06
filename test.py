#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import sys
import json
import os

file = open("speech.txt","w")

if not os.path.exists("model"):
    print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
    exit (1)


model = Model("model")

# Large vocabulary free form recognition
rec = KaldiRecognizer(model, 16000)

# You can also specify the possible word list
#rec = KaldiRecognizer(model, 16000, "zero oh one two three four five six seven eight nine")

wf = open("speech.mp3", "rb")
wf.read(44) # skip header

while True:
    data = wf.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        print (res['text'])

res = json.loads(rec.FinalResult())
file.write(rec.FinalResult())
comm = str(res['text'][0:])
print (res['text'])
print("Lengt is : ")
print(len(res['text']))

if len(res['text']) >= 3:
    print("audio is not empty")
os.system("python pec_audio.py")
print("recognition done")

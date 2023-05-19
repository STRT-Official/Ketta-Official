import os
import pathlib 
from pathlib import Path
from playsound import playsound
import subprocess, sys
import numpy as np
import seaborn as sns
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import models

seed = 42
tf.random.set_seed(seed)
np.random.seed(seed)


def get_spectrogram(waveform):
  # Convert the waveform to a spectrogram via a STFT.
  spectrogram = tf.signal.stft(
      waveform, frame_length=255, frame_step=128)
  # Obtain the magnitude of the STFT.
  spectrogram = tf.abs(spectrogram)
  # Add a `channels` dimension, so that the spectrogram can be used
  # as image-like input data with convolution layers (which expect
  # shape (`batch_size`, `height`, `width`, `channels`).
  spectrogram = spectrogram[..., tf.newaxis]
  return spectrogram
  
  
model = tf.saved_model.load('model/')

def pred():
    if Path('recorded').is_file():
        dic = model('r.wav')
        print(dic)
        val = dic["class_names"]
        val = str(val)
        del dic
        if val=="tf.Tensor([b'heyketta'], shape=(1,), dtype=string)" :
            print("Wake Word presence : Affirmative")
            os.remove('recorded')
            playsound('recog.mp3')
            f=open('torecog', "w")
            f.close()
            os.execl(sys.executable, sys.executable, *sys.argv)
            
        else:
            print("Wake Word presence : Negative")
            os.remove('recorded')
            os.execl(sys.executable, sys.executable, *sys.argv)
        

while True:
    pred()


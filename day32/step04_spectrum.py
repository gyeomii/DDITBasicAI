import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa
from day02.step02_trim import cutMute
fig, ax = plt.subplots()
files = os.listdir("./res")
cnt=1
# for f in files: 
y, sr = librosa.load(f"./res/기민혁마1.mp3")
y_trim = cutMute(y)

# plt.specgram(y_trim)
# plt.show()

D = librosa.amplitude_to_db(np.abs(librosa.stft(y_trim)), ref=np.max)
librosa.display.specshow(D, y_axis='linear', x_axis='time', sr=sr)

plt.show()
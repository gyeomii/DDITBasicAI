import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa
from day03.trim import cutMute

files = os.listdir("./record/k")
cnt=1
for f in files: 
    y, sr = librosa.load(f"./record/k/{f}")
    
    y_trim = cutMute(y)
    
    t = np.arange(0,len(y_trim))
    plt.plot(t,y_trim)
    plt.grid()
    plt.show()

import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa
from day03.trim import cutMute

files = os.listdir("./record/k_test")
for idx,f in enumerate(files):
    f_name = f.split(".")[0] 

    y, sr = librosa.load(f"./record/k_test/{f}")
    y_trim = cutMute(y)
    
    plt.specgram(y_trim)
    
    plt.savefig(f'./test/{f_name}.png')
    print(idx)
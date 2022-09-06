import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa
from day02.step02_trim import cutMute

files = os.listdir("./res")
cnt=1
for f in files: 
    y, sr = librosa.load(f"./res/{f}")
    
    y_trim = cutMute(y)
    
    t = np.arange(0,len(y_trim))
    plt.plot(t,y_trim)
    plt.grid()
    # plt.show()
    plt.savefig(f'./image/{cnt}.png')
    cnt+=1
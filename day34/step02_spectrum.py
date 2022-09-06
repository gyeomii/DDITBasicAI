import os
import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa
import sklearn.preprocessing
from day04.trim import cutMute

files = os.listdir("./record")
for idx,f in enumerate(files):
    f_name = f.split(".")[0] 

    y, sr = librosa.load(f"./record/{f}", sr=16000)
    
    y_trim = cutMute(y)
    
    # print('sr:', sr, ', audio shape:', y_trim.shape)
    # print('length:', y_trim.shape[0]/float(sr), 'secs')
    #
    # mfcc = librosa.feature.mfcc(y_trim, sr=16000, n_mfcc=200, n_fft=400, hop_length=160)
    # mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
    
    plt.specgram(y_trim)

    plt.savefig(f'./train/{f_name}.png')
    print(idx)
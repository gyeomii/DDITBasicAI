import matplotlib.pyplot as plt
import os
from scipy.io import wavfile
from collections import defaultdict, Counter
from scipy import signal
import numpy as np
import librosa
import random as rn
from keras.layers import Dense
from keras import Input
# from keras.engine import Model
# from keras.utils import to_categorical
from keras.layers import Dense, TimeDistributed, Dropout, Bidirectional, GRU, BatchNormalization, Activation, LeakyReLU, LSTM, Flatten, RepeatVector, Permute, Multiply, Conv2D, MaxPooling2D



pad1d = lambda a, i: a[0: i] if a.shape[0] > i else np.hstack((a, np.zeros(i - a.shape[0])))
pad2d = lambda a, i: a[:, 0: i] if a.shape[1] > i else np.hstack((a, np.zeros((a.shape[0],i - a.shape[1]))))


#sr : 오디오의 초당 샘플링 수, wav : 시계열 데이터
wav, sr = librosa.load("luck.wav")

padded_x = pad1d(wav, 30000)
spectrogram = np.abs(librosa.stft(wav))
padded_spectogram = pad2d(spectrogram,40)

mfcc = librosa.feature.mfcc(wav)
padded_mfcc = pad2d(mfcc,40)

print('sr:', sr)
print('wav shape:', wav.shape)
print('padded_x shape:', padded_x.shape)
print('spectrogram shape:', spectrogram.shape)
print('padded_spectogram shape:', padded_spectogram.shape)
print('mfcc shape:', mfcc.shape)
print('padded_mfcc shape:', padded_mfcc.shape)

print('mfcc:', mfcc)
print('padded_mfcc:', padded_mfcc)

print('length:', wav.shape[0]/float(sr), 'secs')

plt.plot(padded_mfcc)
plt.show()

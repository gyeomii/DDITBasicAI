import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
import sklearn.preprocessing
from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical
from tensorboard.compat import tf
import numpy as np
import cv2
#------------------------------------------------------------------------------step6

def cutMute(arr_n):
    idx_f = 0
    while True:
        if arr_n[idx_f]<0.03:
            pass
        else:
            break
        idx_f+=1
        
    idx_f-=40
    
    
    idx_l = len(arr_n)-1
    while True:
        if arr_n[idx_l]<0.03:
            pass
        else:
            break
        idx_l-=1
        
    idx_l+=40
    
    return arr_n[idx_f:idx_l]


y, sr = librosa.load("record/박지영안1.mp3", sr=16000)
    
y_trim = cutMute(y)

print('sr:', sr, ', audio shape:', y_trim.shape)
print('length:', y_trim.shape[0]/float(sr), 'secs')

mfcc = librosa.feature.mfcc(y_trim, sr=16000, n_mfcc=200)
mfcc = sklearn.preprocessing.scale(mfcc, axis=1)
t = np.arange(0, len(mfcc))
print(sr)
print(mfcc)

plt.specgram(mfcc)
plt.savefig("output.png")
plt.title('Spectrogram Using matplotlib.pyplot.specgram() method')  
plt.show() 

#------------------------------------------------------------------------------step7




labels = [
          "기민혁",          
          "김성겸",
          "박수빈",
          "박지영",
          "윤재열",
          "채희진"
          ]

img1 = cv2.imread('output.png')
print("img1",img1.shape)
train_images = img1.reshape((1,480,640,3))
train_images = train_images/255.0




model = tf.keras.models.load_model('teamVoice3.h5')

predictions = model.predict(train_images)
l_idx = np.argmax(predictions[0])

print(l_idx,labels[l_idx])
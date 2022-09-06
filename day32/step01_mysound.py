import numpy as np
import matplotlib.pyplot as plt
import librosa.display, librosa

y, sr = librosa.load("./res/김성겸가1.mp3")
t = np.arange(0,len(y))
plt.plot(t,y)
plt.grid()
plt.show()
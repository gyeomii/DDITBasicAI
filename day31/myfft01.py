import numpy as np
import matplotlib.pyplot as plt
 
fs = 100
t = np.arange(0, 3, 1 / fs)
f1 = 10
f2 = 35
signal = 0.01 * np.sin(2 * np.pi * f1 *t) + 0.01 * np.cos(2 * np.pi * f2 *t)
 
fft = np.fft.fft(signal) #/ len(signal)  
 
fft_magnitude = abs(fft)

plt.subplot(2,1,1)
plt.plot(t,signal)
plt.grid()
 
plt.subplot(2,1,2)
plt.stem(fft_magnitude)
plt.ylim(0,2.5)
plt.grid()
plt.show()

length = len(signal)
f = np.linspace(-(fs / 2), fs / 2, length)   
 
plt.stem(f, np.fft.fftshift(fft_magnitude)) 
plt.ylim(0,2.5)
plt.grid()
 
plt.show()
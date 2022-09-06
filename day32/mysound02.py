from scipy.io import wavfile
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt


sample_rate, samples = wavfile.read("download.wav")

print('sample rate : {}, samples.shape : {}'.format(sample_rate, samples.shape))
# sample_rate = sample_rate[:16000]


def log_specgram(audio, sample_rate, window_size=20, step_size=10, eps=1e-10):
    # nperseg: Length of each segment
    # noverlap: Number of points to overlap between segments
    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    freqs, times, spec = signal.spectrogram(audio, fs=sample_rate,
                                            window='hann', nperseg=nperseg,
                                            noverlap=noverlap, detrend=False)
    return freqs, times, np.log(spec.T.astype(np.float32) + eps)

freqs, times, spectrogram = log_specgram(samples, sample_rate)

fig = plt.figure(figsize=(14, 8))
ax1 = fig.add_subplot(211)
ax1.set_title('Raw wave of ' )
ax1.set_ylabel('Amplitude')
ax1.plot(np.linspace(0, sample_rate/len(samples), sample_rate), samples)

ax2 = fig.add_subplot(212)
ax2.imshow(spectrogram.T, aspect='auto', origin='lower',
           extent=[times.min(), times.max(), freqs.min(), freqs.max()])
ax2.set_yticks(freqs[::16])
ax2.set_xticks(times[::16])
ax2.set_title('Spectrogram of ' )
ax2.set_ylabel('Freqs in Hz')
ax2.set_xlabel('Seconds')



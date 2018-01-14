import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wave

rate,data = wave.read('sound5.wav')
spectre = np.fft.fft(data)
freq = np.fft.fftfreq(data.size, 1/rate)
mask=freq>0
plt.plot(freq[mask],np.abs(spectre[mask]))
import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('sound.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

silenced=signal[0:50000]

#If Stereo
if spf.getnchannels() == 2:
    sys.exit(0)


Time=np.linspace(0, len(silenced)/fs, num=len(silenced))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,silenced)
plt.show()
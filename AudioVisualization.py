import matplotlib.pyplot as plt
import numpy as np
import wave
from getTimeLength import getSoundLength
import statistics
import sys


file = 'sound5.wav'

with wave.open(file,'r') as wav_file:
    #Extract Raw Audio from Wav File
    signal = wav_file.readframes(-1)
    signal = np.fromstring(signal, 'Int16')

    pitch = 0

    dist = int(len(signal)/(100*getSoundLength()))
    j = 0
    dats = []
    for i in range(dist, len(signal), dist):
        m = max(signal[j:i])
        dats.append(m)
        j = i
    medianSound = (np.median(dats))
    backgroundSoundThreshold = medianSound + 1000

    for i in signal:
        if i>= backgroundSoundThreshold:
            pitch = pitch + 1
    print(pitch)










    #Split the data into channels
    channels = [[] for channel in range(wav_file.getnchannels())]
    for index, datum in enumerate(signal):
        channels[index%len(channels)].append(datum)

    #Get time from indices
    fs = wav_file.getframerate()
    Time=np.linspace(0, len(signal)/len(channels)/fs, num=len(signal)/len(channels))

    #Plot
    plt.figure(1)
    plt.title('Signal Wave...')
    for channel in channels:
        plt.plot(Time,channel)
    plt.show()
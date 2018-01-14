import matplotlib.pyplot as plt
import numpy as np
import wave
from getTimeLength import getSoundLength
import statistics
import sys


file = 'sound3.wav'
file2 = 'sound5.wav'

def createGraph(file):
    with wave.open(file,'r') as wav_file:
        #Extract Raw Audio from Wav File
        signal = wav_file.readframes(-1)
        signal = np.fromstring(signal, 'Int16')

        k = round(float(max(signal[0:5000])+500) / 1000.0) * 1000.0

        print(k)

        count = 0
        for wavelength in signal:
            if wavelength >= k:
                count += 1


        print(count/getSoundLength(file))
        """ 
        dist = int(len(signal)/(300*getSoundLength()))
        j = 0
        dats = []
        for i in range(dist, len(signal), dist):
            m = max(signal[j:i])
            dats.append(round(m / 1000.0) * 1000.0)
            j = i
        #print(dats)
        medianSound = (np.median(dats))

        print(medianSound)

        backgroundSoundThreshold = medianSound + 1000

        #print(backgroundSoundThreshold)
"""


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
        

        


createGraph(file)
createGraph(file2)

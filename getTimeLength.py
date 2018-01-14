import soundfile as sf
from speechToText import getText

def getSoundLength():
    f = sf.SoundFile('sound.wav')
    return(len(f) / f.samplerate)

print(getSoundLength())

wpm = len(getText().strip(' ').split(' '))/(getSoundLength()/60.0)
print(wpm)
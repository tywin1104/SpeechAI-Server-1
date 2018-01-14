import soundfile as sf
from speechToText import getText

def getSoundLength():
    f = sf.SoundFile('test.wav')
    return(len(f) / f.samplerate)


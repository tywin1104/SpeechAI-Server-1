import soundfile as sf


def getSoundLength():
    f = sf.SoundFile('test.wav')
    return(len(f) / f.samplerate)


from pydub import AudioSegment

def getSoundLoudness(name):
    song = AudioSegment.from_wav(name)
    print(song.dBFS)
    if song.dBFS >= -18.5:
        return "loud"
    else:
        return "quiet"



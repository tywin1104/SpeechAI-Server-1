import pydub.audio_segment
from pydub import AudioSegment

def getSoundLength(name):

    song = AudioSegment.from_wav(name)
    return (song.duration_seconds)




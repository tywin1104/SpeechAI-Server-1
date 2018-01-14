
import pydub.audio_segment

def getSoundLength():
    from pydub import AudioSegment

    song = AudioSegment.from_wav("test.wav")
    return(song.duration_seconds)

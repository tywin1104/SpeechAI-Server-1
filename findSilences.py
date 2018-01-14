from pydub import AudioSegment
from pydub.silence import detect_silence


def findSilences(recordedText):
    count = round(len(recordedText.split(" "))/6)

    sound_file = AudioSegment.from_wav("test.wav")
    det = detect_silence(sound_file,  # must be silent for at least half a second
        min_silence_len=500,
        # consider it silent if quieter than -16 dBFS
        silence_thresh=sound_file.dBFS)

    print(det)

    if (len(det) <= (count + 2)) & (len(det) >= (count - 2)):
        return 'Good'
    elif (len(det) < (count - 2)):
        return 'Fast'
    else:
        return 'Slow'


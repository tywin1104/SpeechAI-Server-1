from pydub import AudioSegment
from pydub.silence import detect_silence


def findSilences(recordedText):
    count = round(len(recordedText.split(" "))/6)

    sound_file = AudioSegment.from_wav("test.wav")
    det = detect_silence(sound_file,  # must be silent for at least half a second
        min_silence_len=500,
        # consider it silent if quieter than -16 dBFS
        silence_thresh=sound_file.dBFS)

    detCount = len(det)
    diff = 0
    if detCount < (count-2):
        diff = (detCount/(count-2))
    elif detCount > (count+2):
        diff = abs((count-2) - ((count+2)-detCount))

    if (len(det) <= (count + 2)) & (len(det) >= (count - 2)):
        return ['good',diff]
    elif (len(det) < (count - 2)):
        return ['fast',diff]
    else:
        return ['slow',diff]


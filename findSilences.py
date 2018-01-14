from pydub import AudioSegment
from pydub.silence import detect_silence
sound_file = AudioSegment.from_wav("sound.wav")
sound_file
det = detect_silence(sound_file,  # must be silent for at least half a second
    min_silence_len=500,
    # consider it silent if quieter than -16 dBFS
    silence_thresh=sound_file.dBFS)
print(det)

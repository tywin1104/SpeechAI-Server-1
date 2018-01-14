import speech_recognition as sr

def getText(text):

    AUDIO_FILE = text

    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Microsoft Bing Voice Recognition
    BING_KEY = "a5ba1c9bd35c4f8589084b5a7356040a"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        return (r.recognize_bing(audio, key=BING_KEY))
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))
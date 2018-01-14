from speechToText import getText
from getTimeLength import getSoundLength

def getWordsPerMinute(recordedText):
    return(len(recordedText.strip(' ').split(' ')) / (getSoundLength('test.wav') / 60.0))

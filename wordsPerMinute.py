from speechToText import getText
from getTimeLength import getSoundLength

def getWordsPerMinute(recordedText):
    return(len(recordedText.strip(' ').split(' ')) / (getSoundLength() / 60.0))

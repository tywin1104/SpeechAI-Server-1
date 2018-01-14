from speechToText import getText
from getTimeLength import getSoundLength

def getWordsPerMinute():
    wpm = len(getText().strip(' ').split(' ')) / (getSoundLength() / 60.0)
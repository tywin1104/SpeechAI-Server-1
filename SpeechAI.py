from flask import Flask
from flask import request
from io import BytesIO
import requests
from speechToText import getText
from diffChecker import similar
from getTimeLength import getSoundLength
from wordsPerMinute import getWordsPerMinute
import firebase

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api')
def getAudio():
    recordingID = request.args.get('id')
    file = BytesIO()
    mp3 = requests.get('gs://speechai2.appspot.com/test.mp3')

    actualText = "Get from firebase"
    similarity = similar(actualText, getText())
    wpm = getWordsPerMinute()
    print(wpm)


    






if __name__ == '__main__':
    app.run()

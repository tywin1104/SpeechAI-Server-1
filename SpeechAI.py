from flask import Flask
from flask import request
from speechToText import getText
from diffChecker import similar
from wordsPerMinute import getWordsPerMinute
from firebase import firebase
import urllib.request
from findSilences import findSilences
import json

DEBUG = True
app = Flask(__name__)

firebase = firebase.FirebaseApplication('https://speechai2.firebaseio.com', None)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/api', methods=['GET'])
def getAudio():
    userID = request.args.get('userId')
    recordingID = request.args.get('speechId')


    print("https://speechai2.firebaseio.com"+'/users/'+userID+'/speeches/'+recordingID)

    recordingData = firebase.get('/users/'+userID+'/speeches/'+recordingID, None)
    print(recordingData)

    actualText = recordingData['text']
    recordingURL = recordingData['url']

    file_name = "test.wav"
    rsp = urllib.request.urlopen(recordingURL)
    with open(file_name, "wb") as f:
       f.write(rsp.read())

    recordedText = getText("test.wav")

    pausing = findSilences(recordedText)
    similarity = similar(actualText, getText("test.wav"))
    wpm = getWordsPerMinute(recordedText)
    print(wpm)

    data = {'wpm':wpm, 'similarity':similarity, 'pausing':pausing}
    return json.dumps(data)


if __name__ == '__main__':
    app.run()

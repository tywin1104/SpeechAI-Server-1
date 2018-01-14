from flask import Flask
from flask import request
from speechToText import getText
from diffChecker import similar
from wordsPerMinute import getWordsPerMinute
from getLoudness import getSoundLoudness
from firebase import firebase
import urllib.request
from findSilences import findSilences
import json
from random import *

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

    lastData = firebase.get('/users/'+userID+'/lastData/', None)
    recordingData = firebase.get('/users/'+userID+'/speeches/'+recordingID, None)
    print(recordingData)

    actualText = recordingData['text']
    recordingURL = recordingData['url']

    file_name = "test.wav"
    rsp = urllib.request.urlopen(recordingURL)
    with open(file_name, "wb") as f:
       f.write(rsp.read())

    recordedText = getText(file_name)

    pausing = findSilences(recordedText)
    similarity = similar(actualText, getText(file_name))
    wpm = int(getWordsPerMinute(recordedText))
    loudness = getSoundLoudness(file_name)
    print(wpm)

    score = 0.0
    if wpm >= 120 and wpm <= 170:
        score += .25
    else:
        score += randint(10,15)/100
    score += similarity * .25
    if pausing == 'good':
        score += .25
    else:
        score += randint(10,15)/100
    if loudness == 'quiet':
        score += randint(10,15)/100
    else:
        score += .25

    if lastData['wpm'] != 'pass':
        p = True
        if pausing == 'slow' or pausing == 'fast':
            p = False
        elif pausing == lastData['pausing']:
            p = 'same'

        l = True
        if lastData['loudness'] == loudness:
            l = 'same'
        elif lastData['loudness'] == 'loud' and loudness=='quiet':
            l = False

        pastData = {'wpm': (wpm > lastData['wpm']), 'similarity': (similarity > lastData['similarity']), 'pausing':p, 'loudness':l}
    else:
        pastData = {'wpm': 'pass', 'similarity': 'pass', 'pausing': 'pass', 'loudness':'pass'}
    currentData = {'wpm': wpm, 'similarity': similarity, 'pausing': pausing, 'loudness': loudness}
    scorePastData = {'score':score, 'pastData':pastData}
    data = {**currentData, **scorePastData}

    result = firebase.put('/users/'+userID, 'lastData', currentData)

    return json.dumps(data)


if __name__ == '__main__':
    app.run()

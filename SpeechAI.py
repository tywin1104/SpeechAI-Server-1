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

    #Pausing Data
    pausingData = findSilences(recordedText)
    pausing, pausingVal = pausingData[0], pausingData[1]

    #Similarity Data
    similarity = similar(actualText, getText(file_name))

    #WPM Data
    wpm = int(getWordsPerMinute(recordedText))

    #Loudness Data
    loudnessData = getSoundLoudness(file_name)
    loudness,loudVal = loudnessData[0], loudnessData[1]

    print(wpm)

    score = 0.0

    # WPM Calculation
    if wpm >= 120 and wpm <= 170:
        score += .25
    elif wpm < 120:
        diff = 120-wpm
        score += (diff/120) * 0.25
    else:
        diff = abs(120 - (wpm-170))
        score += (diff/120) * 0.25

    # Similarity Calculation
    score += similarity * .25

    # Pausing Calculation
    if pausing == 'good':
        score += .25
    else:
        score += .25 * (pausingVal)

    # Loudness Calculation
    if loudness == 'good':
        score += .25
    else:
        diff = 18.5-abs(loudVal)
        score += .25 * (diff/18.5)

    if lastData['wpm'] != 'pass':
        p = True
        if pausing == 'slow' or pausing == 'fast':
            p = False
        l = True
        if lastData['loudness'] == 'loud' and loudness=='quiet':
            l = False

        pastData = {'wpm': (wpm > lastData['wpm']), 'similarity': (similarity > lastData['similarity']), 'pausing':p, 'loudness':l}
    else:
        pastData = {'wpm': False, 'similarity': False, 'pausing': False, 'loudness':False}
    currentData = {'wpm': wpm, 'similarity': similarity, 'pausing': pausing, 'loudness': loudness}
    scorePastData = {'score':score, 'pastData':pastData}
    allData = {**currentData, **{'score':score}}
    data = {**currentData, **scorePastData}

    result = firebase.put('/users/'+userID, 'lastData', currentData)
    speechData = firebase.put('/users/'+userID+'/speeches/'+recordingID, 'data',allData)

    return json.dumps(data)


if __name__ == '__main__':
    app.run()

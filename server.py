
'''
Module to perform emotion detection.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detect():
    '''
function to perform the emotion detection
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'None':
        return 'Invalid text, please try again!'
    return response

@app.route("/")
def render_index_page():
    '''
function to render the index.html page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)

import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=headers)
    formatted_text= json.loads(response.text)

    
    if response.status_code == 200:
        emotion = formatted_text["emotionPredictions"][0]["emotion"]
        sorted_emotion = sorted(emotion.items(), key=lambda x:x[1], reverse=True)
        final = dict(sorted_emotion)
        emotion['dominant_emotion'] = list(final.keys())[0]

    elif response.status_code == 400:
        emotion = {
         'anger': 'None',
         'disgust': 'None',
         'fear': 'None',
         'joy': 'None',
         'sadness': 'None',
         'dominant_emotion': 'None'
        }

    return emotion
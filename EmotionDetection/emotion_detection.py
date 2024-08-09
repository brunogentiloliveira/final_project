import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    result = requests.post(url, json = myobj, headers = header)

    formatted_response = json.loads(result.text)

    emotions = formatted_response['emotionPredictions'][0]

    anger = emotions['emotion']['anger']
    disgust = emotions['emotion']['disgust']
    fear = emotions['emotion']['fear']
    joy = emotions['emotion']['joy']
    sadness = emotions['emotion']['sadness']

    emotions_dict = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }

    max_tmp = max(emotions_dict, key=emotions_dict.get)
    emotions_dict['dominant_emotion'] = max_tmp

    return emotions_dict
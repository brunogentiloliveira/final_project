from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("EmotionDetector")

@app.route("/emotionDetector")
def emotion_detection():
    text_to_analyze = request.args.get('textToAnalyze)

    
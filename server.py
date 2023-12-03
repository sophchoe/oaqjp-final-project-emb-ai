"""
Executing this function initiates the application of emotion
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detect():
    """This code receives the text from the HTML interface and runs emotion detectioin over it"""
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    if result is None:
        return "Invalid input! Try again."
    res1 = f"For the given statement, the system response is {result}."
    res2 = f"The dominant emotion is \033[1m{result['dominant_emotion']}\033[0m."
    return res1 + res2

@app.route("/")
def render_index_page():
    """Initiates the rendering of the main application page over the Flask channel"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

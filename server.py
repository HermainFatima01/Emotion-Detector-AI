"""
server.py

Flask web application that serves an HTML page with a text box and
exposes an /emotionDetector endpoint used to analyse the emotional
content of user-submitted text via the EmotionDetection package.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    """
    Reads the 'textToAnalyze' query parameter, runs emotion detection
    on it, and returns a formatted sentence describing the result.
    Returns an error message if the input text is invalid/blank.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Task 7: Handle invalid/blank input gracefully.
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!", 400

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """Serves the main HTML page containing the text-entry UI."""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

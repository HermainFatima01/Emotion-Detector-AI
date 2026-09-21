"""
emotion_detection.py

This module provides a function to detect emotions in a given piece of
text using the Watson NLP EmotionPredict service. It formats the raw
service response into a clean dictionary containing the score for each
emotion plus the dominant (highest-scoring) emotion, and it gracefully
handles invalid input.
"""

import json
import requests


def emotion_detector(text_to_analyse):
    """
    Sends the given text to the Watson NLP EmotionPredict service and
    returns a dictionary with the scores for anger, disgust, fear, joy,
    and sadness, along with the dominant emotion.

    Parameters:
        text_to_analyse (str): The text to run emotion detection on.

    Returns:
        dict: {
            'anger': float or None,
            'disgust': float or None,
            'fear': float or None,
            'joy': float or None,
            'sadness': float or None,
            'dominant_emotion': str or None
        }
        All values are None if the input text is blank/invalid
        (i.e. the service returns a 400 status code).
    """
    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyse}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    # Task 7: Error handling for blank/invalid input.
    # Watson NLP returns HTTP 400 when the input text is empty or invalid.
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Task 3: Format the output and determine the dominant emotion.
    emotion_scores = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    final_output = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }

    return final_output

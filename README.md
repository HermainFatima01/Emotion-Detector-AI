**Emotion Detector
A web application that detects the emotions (anger, disgust, fear, joy, sadness) expressed in a piece of text, built using the Watson NLP library and deployed with Flask.
This project was built as a final project for an AI Application Development course, covering the full development lifecycle: building the core detection logic, formatting output, packaging, unit testing, web deployment, error handling, and static code analysis.
Features
Detects 5 emotions in a given text: anger, disgust, fear, joy, sadness
Identifies the dominant emotion (the one with the highest score)
Simple web UI with a text box to enter text and see results
Graceful error handling for blank/invalid input
Fully unit tested
Passes static code analysis (Pylint score: 10/10)
Project Structure
```
emotion_detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py     # Core emotion detection logic
├── templates/
│   └── index.html               # Web UI
├── static/
│   ├── mywebscript.js           # Front-end JS (calls the API)
│   └── style.css                # Styling
├── test_emotion_detection.py    # Unit tests
├── server.py                    # Flask web server
└── requirements.txt             # Python dependencies
```
Setup
Clone this repository:
```
   git clone https://github.com/yourusername/emotion-detector.git
   cd emotion-detector
   ```
Install dependencies:
```
   pip install -r requirements.txt
   ```
Running the App
Start the Flask server:
```
python3 server.py
```
Then open your browser and go to:
```
http://localhost:5000
```
Type a sentence into the text box and click Analyze to see the detected emotions and the dominant emotion.
Running Tests
Run the unit test suite:
```
python3 -m unittest test_emotion_detection.py -v
```
> **Note:** The tests call the Watson NLP EmotionPredict service over the network, so an internet connection (and access to `sn-watson-emotion.labs.skills.network`) is required for them to pass.
Running Static Code Analysis
```
pylint EmotionDetection/emotion_detection.py server.py test_emotion_detection.py
```
How It Works
The user enters text in the web page and clicks Analyze.
The front-end JavaScript sends the text to the `/emotionDetector` Flask route.
`emotion_detector()` sends the text to the Watson NLP EmotionPredict API.
The response is parsed into scores for each emotion, and the dominant emotion is calculated.
The result is formatted and sent back to display on the page.
If the input text is blank or invalid, the app returns a friendly error message instead of crashing.
Tech Stack
Python — core logic and server
Flask — web framework
Watson NLP (EmotionPredict) — emotion detection model
HTML/CSS/JavaScript — front-end
unittest — testing
Pylint — static code analysis
License
This project is for educational purposes.**

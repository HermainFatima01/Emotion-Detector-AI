// mywebscript.js
// Sends the textarea content to the /emotionDetector endpoint and
// displays the formatted response (or an error message) on the page.

function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            const responseEl = document.getElementById("system_response");
            if (this.status === 200) {
                responseEl.innerText = this.responseText;
            } else {
                responseEl.innerText = "Invalid text! Please try again!";
            }
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
}

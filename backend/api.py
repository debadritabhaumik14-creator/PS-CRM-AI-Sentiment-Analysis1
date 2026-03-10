from flask import Flask, request, jsonify
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    sentiment = analyze_sentiment(text)
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(debug=True)

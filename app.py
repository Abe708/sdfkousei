from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # フロントエンドとの通信を許可

correction_table = {
    "こんにちわ": "こんにちは",
    "有難う御座います": "ありがとうございます",
    "すごい良い": "とても良い"
}

@app.route('/check', methods=['POST'])
def check_text():
    data = request.json
    text = data.get("text", "")

    suggestions = []
    for word, replacement in correction_table.items():
        if word in text:
            suggestions.append({
                "original": word,
                "suggestion": replacement,
                "index": text.index(word)
            })

    return jsonify({"suggestions": suggestions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

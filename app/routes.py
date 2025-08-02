from flask import Blueprint, request, jsonify

bp = Blueprint('api', __name__)

@bp.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = {
        "word_count": len(text.split()),
        "char_count": len(text),
        "sentiment": "positive" if "good" in text.lower() else "neutral"
    }
    return jsonify(result)

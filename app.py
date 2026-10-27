from pathlib import Path
import os
from dotenv import load_dotenv
from flask import Flask, jsonify, request

# Load secrets from the .env file beside this script
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path)

app = Flask(__name__)

API_KEYS = {
    os.getenv("CONSUMER_1_KEY"): "Consumer 1",
    os.getenv("CONSUMER_2_KEY"): "Consumer 2",
    os.getenv("CONSUMER_3_KEY"): "Consumer 3",
}

# Remove missing or empty keys
API_KEYS = {
    key: consumer
    for key, consumer in API_KEYS.items()
    if key
}


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Text Processing API is running"
    }), 200


@app.route("/process", methods=["POST"])
def process_text():
    api_key = request.headers.get("X-API-Key")

    if not api_key or api_key not in API_KEYS:
        return jsonify({
            "error": "Invalid or missing API key"
        }), 401

    data = request.get_json(silent=True)
 

    if not isinstance(data, dict) or not isinstance(data.get("text"), str):
        return jsonify({
            "error": "Please provide a JSON object containing a text string"
        }), 400

    return jsonify({
        "consumer": API_KEYS[api_key],
        "original_text": data["text"],
        "processed_text": data["text"].upper()
    }), 200


if __name__ == "__main__":
    print("Starting Text Processing API...")
    print(f"Configured consumer keys: {len(API_KEYS)}")
    app.run(host="127.0.0.1", port=5000, debug=False)
print("Starting Text Processing API...")

print(f"Configured consumer keys:{len(API_KEYS) }")

app.run(host="127.0.0.1", port=5000, debug=False)
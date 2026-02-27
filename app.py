from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()
    phone = data.get("number")

    if not phone:
        return jsonify({"status": "error", "message": "No number"})

    return jsonify({
        "status": "success",
        "data": f"Test response for {phone}"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# app.py

from flask import Flask, request, jsonify
from script import run_tool

app = Flask(__name__)
@app.route("/ping", methods=["GET"])
def ping():
    return "PING OK"
@app.route("/", methods=["GET"])
def home():
    return "Backend is running"

@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    phone = data.get("number")

    if not phone or not phone.isdigit() or len(phone) != 10:
        return jsonify({
            "status": "error",
            "message": "Invalid phone number"
        })

    try:
        result = run_tool(phone)
        return jsonify({
            "status": "success",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run()

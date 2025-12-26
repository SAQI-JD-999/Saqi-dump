from flask import Flask, request, jsonify
import time

app = Flask(__name__)
APPROVED = {}

@app.route("/check", methods=["POST"])
def check():
    device = request.json.get("device")
    if device in APPROVED:
        return jsonify({
            "status": "OK",
            "expiry": APPROVED[device]
        })
    return jsonify({"status": "DENIED"})

app.run(host="0.0.0.0", port=10000)

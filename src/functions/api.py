import json

from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/calculate/run", methods=["GET"])
def calculate_run():
    return jsonify({
        'status': 'SUCCESS',
        'calories': 1200
    }), 200

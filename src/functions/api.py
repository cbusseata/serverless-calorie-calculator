import json

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        'status': 'SUCCESS',
        'message': 'Hello World!'
    }), 200

@app.route("/calculate/run")
def calculate_run():
    return jsonify({
        'status': 'SUCCESS',
        'calories': 1200
    }), 200

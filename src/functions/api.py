import json

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({
        'status': 'SUCCESS',
        'message': 'Hello World!'
    }, 200)

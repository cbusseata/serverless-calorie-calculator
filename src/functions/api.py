import json
from flask_wtf import FlaskForm
from wtforms import fields, validators

from flask import Flask, request, jsonify
app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = False

class CalculateRunForm(FlaskForm):
    distance = fields.FloatField(
        'Distance', 
        validators=[
            validators.DataRequired(),
            validators.NumberRange(min=0.01, message="Come on, distance must be at least %(min)s miles!")
        ]
    )
    #time
    weight = fields.FloatField(
        'weight', 
        validators=[
            #validators.DataRequired(),
            validators.Optional(), # @TODO: for now...
            validators.NumberRange(min=0.01, message="Weight must be at least %(min)s pounds")
        ]
    )
    elevation_gain = fields.IntegerField(
        'elevation_gain',
        validators=[
            # Not sure about this one yet
            #validators.DataRequired(),
            validators.Optional(), # @TODO: for now...
            validators.NumberRange(min=0, message="Elevation gain must be at least %(min)s feet")
        ]
    )

@app.route("/calculate/run", methods=["GET"])
def calculate_run():
    form = CalculateRunForm(request.args)
    if not form.validate():
        return jsonify({
            'status': 'ERROR',
            'errors': form.errors,
            'args': request.args
        }), 400

    return jsonify({
        'status': 'SUCCESS',
        'calories': 1200
    }), 200

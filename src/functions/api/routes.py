import os
import sys
import json
from datetime import timedelta
from flask import request, jsonify
from measurement.measures import Distance, Mass
from . import app, forms

# We need this so that the proper modules can be found in AWS context
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from src.domain import activity, calorie_calculator, vo2


@app.route("/calculate/<string:act>", methods=["GET"])
def calculate_run(act):
    # Get the query parameters and merge in the activity
    params = request.args
    params.update({'activity': act})

    form = forms.CalculateRunForm(params)
    if not form.validate():
        return jsonify({
            'status': 'ERROR',
            'errors': form.errors
        }), 400

    try:
        calories = calorie_calculator.calculate_calories_burned(
            activity=getattr(activity, act.capitalize())(),
            # Distance in miles or kilometers, depending on "units" value
            distance=Distance(**{'mi' if form.units.data == 'imperial' else 'km': form.distance.data}),
            # Bodyweight in pounds or kilograms, depending on "units" value
            bodyweight=Mass(**{'lb' if form.units.data == 'imperial' else 'kg': form.bodyweight.data}),
            # Elevation gain in meters or feet, depending on "units" value
            elevation_gain=Distance(**{'ft' if form.units.data == 'imperial' else 'm': form.elevation_gain.data}),
            duration=timedelta(
                hours=int(form.hours.data),
                minutes=int(form.minutes.data),
                seconds=int(form.seconds.data)
            )
        )
    except Exception as e:
        return jsonify({
            'status': 'ERROR',
            'message': str(e),
        }), 500

    return jsonify({
        'status': 'SUCCESS',
        'calories': calories,
    }), 200

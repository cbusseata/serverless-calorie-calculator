import json
from datetime import timedelta
from flask import request, jsonify
from . import app, forms


@app.route("/calculate/run", methods=["GET"])
def calculate_run():
    form = forms.CalculateRunForm(request.args)
    if not form.validate():
        return jsonify({
            'status': 'ERROR',
            'errors': form.errors,
        }), 400

    duration = timedelta(
        hours=0 if not request.args.get('hours') else int(request.args.get('hours')), 
        minutes=0 if not request.args.get('minutes') else int(request.args.get('minutes')), 
        seconds=0 if not request.args.get('seconds') else int(request.args.get('seconds'))
    )

    return jsonify({
        'status': 'SUCCESS',
        'calories': 1200,
    }), 200

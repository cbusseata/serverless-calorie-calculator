from flask_wtf import FlaskForm
from wtforms import fields, validators


# Total calories burned = Duration (in minutes)*(MET*3.5*weight in kg)/200
class CalculateRunForm(FlaskForm):
    distance = fields.FloatField(
        'Distance', 
        validators=[
            validators.DataRequired(),
            validators.NumberRange(
                min=0.01, 
                message="Come on, distance must be at least %(min)s miles!"
            )
        ]
    )
    # Duration
    hours = fields.IntegerField(
        'Hours',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ]
    )
    minutes = fields.IntegerField(
        'Minutes',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ]
    )
    seconds = fields.IntegerField(
        'Seconds',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ]
    )
    weight = fields.FloatField(
        'Weight', 
        validators=[
            validators.DataRequired(),
            validators.NumberRange(
                min=0.01, 
                message="Weight must be at least %(min)s pounds"
            )
        ]
    )
    """
    # @TODO
    elevation_gain = fields.IntegerField(
        'elevation_gain',
        validators=[
            # Not sure about this one yet
            #validators.DataRequired(),
            validators.Optional(), # @TODO: for now...
            validators.NumberRange(min=0, message="Elevation gain must be at least %(min)s feet")
        ]
    )
    """

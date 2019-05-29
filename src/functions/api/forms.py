from flask_wtf import FlaskForm
from wtforms import fields, validators


class CalculateRunForm(FlaskForm):
    activity = fields.StringField(
        'Activity',
        validators=[
            validators.DataRequired(),
            validators.AnyOf(
                values=['walk', 'run'],
                message="I don't know what nonsense you're doing, but we only support 'walk' and 'run'"
            )
        ]
    )

    distance = fields.FloatField(
        'Distance', 
        validators=[
            validators.DataRequired(),
            validators.NumberRange(
                min=0.01, 
                message="Come on, distance must be at least %(min)s!"
            )
        ]
    )

    # Duration
    hours = fields.IntegerField(
        'Hours',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ],
        default=0
    )
    minutes = fields.IntegerField(
        'Minutes',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ],
        default=0
    )
    seconds = fields.IntegerField(
        'Seconds',
        validators=[
            validators.Optional(),
            validators.NumberRange(min=0) # Cannot be negative
        ],
        default=0
    )

    bodyweight = fields.FloatField(
        'Bodyweight', 
        validators=[
            validators.DataRequired(),
            validators.NumberRange(
                min=0.01, 
                message="Bodyweight must be at least %(min)s"
            )
        ]
    )

    elevation_gain = fields.IntegerField(
        'elevation_gain',
        validators=[
            validators.Optional()
        ],
        default=0
    )
    
    units = fields.StringField(
        'Units',
        validators=[
            validators.Optional(),
            validators.AnyOf(values=['imperial', 'metric'])
        ],
        default='imperial'
    )

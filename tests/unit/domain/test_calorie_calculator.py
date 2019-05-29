import pytest
from domain import activity, vo2, calorie_calculator
from measurement.measures import Distance, Mass
from datetime import timedelta

testdata = [
    # 0 distance and 0 duration, should get 0
    (activity.Walk(), Distance(mi=0), Mass(lb=180), Distance(ft=0), timedelta(seconds=0), 0),
    # 175 lb athlete running a flat 2 miles at an 8 min/mile pace
    (activity.Run(), Distance(mi=2), Mass(lb=175), Distance(ft=0), timedelta(minutes=16, seconds=0), 278),
    # Marathon
    (activity.Run(), Distance(mi=26.2), Mass(lb=180), Distance(ft=0), timedelta(hours=3, minutes=29, seconds=56), 3743),
    # 100 mile ultramarathon
    (activity.Run(), Distance(mi=100), Mass(lb=190), Distance(ft=0), timedelta(hours=21, minutes=56, seconds=56), 15856),
    # Short uphill walk
    (activity.Walk(), Distance(mi=1.5), Mass(lb=165), Distance(ft=100), timedelta(minutes=15, seconds=32), 131),
    # Hiking the incline in Manitou, Colorado
    (activity.Walk(), Distance(km=1.65), Mass(lb=185), Distance(m=620), timedelta(minutes=31, seconds=15), 583),
]

@pytest.mark.parametrize("activity,distance,bodyweight,elevation_gain,duration,expected", testdata)
def test_calculate_calories_burned(activity, distance, bodyweight, elevation_gain, duration, expected):
    assert expected == calorie_calculator.calculate_calories_burned(
        activity=activity,
        distance=distance,
        bodyweight=bodyweight,
        elevation_gain=elevation_gain,
        duration=duration
    )

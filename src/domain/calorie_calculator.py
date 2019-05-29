from . import activity, vo2
from measurement.measures import Distance, Mass, Speed
from datetime import timedelta

def calculate_calories_burned(
    activity: activity.Activity, 
    distance: Distance, 
    bodyweight: Mass, 
    elevation_gain: Distance, 
    duration: timedelta
) -> int:
    """
    Calculates the number of calories (rounded to the nearest integer) burned during an activity.

    The number of calories burned is calculated by taking the VO2 in ml/min/kg, and converting that to
    L/min (multiply by athlete bodyweight in kg and divide by 1000), then multiplying that number by 5
    kCalories/min, and finally multiplying that by the number of minutes.  The result is then rounded
    to the nearest integer.

    Args:
        activity (Activity):
        distance (Distance):
        bodyweight (Mass):
        elevation_gate (Distance):
        duration (timedelta):

    Returns:
        int: The number of calories burned performing the activity
    """
    if distance.ft == 0:
        return 0

    if duration.total_seconds() == 0:
        return 0

    speed = Speed(mph = distance.mi/(duration.total_seconds()/3600))
    grade = elevation_gain.ft/distance.ft
    vo2_est = vo2.get_VO2(activity, speed, grade)
    # Calculate VO2 in Liters/minute
    vo2_l_min = (vo2_est.get_value() * bodyweight.kg)/1000

    return int(round(vo2_l_min * 5 * duration.total_seconds()/60, 0))

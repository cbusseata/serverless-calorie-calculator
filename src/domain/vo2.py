from measurement.measures import Speed
from . import activity

class VO2:
    _value: float
    """float: Estimated VO2 reserve value
    """

    def __init__(self, o2_cost_horiz: float, o2_cost_vert: float, speed: Speed, grade = 0.0):
        """Initializes instance.

        Args:
            o2_cost_horiz (float): Oxygen cost of moving each kg of bodyweight horizontally
            o2_cost_vert (float): Oxygen cost of moving each kg of bodyweight vertically
            speed (Speed): Speed the subject was moving at
            grade (float): Overall % grade of the surface an activity was performed on
        """
        self._value = self._calculate_vo2(o2_cost_horiz, o2_cost_vert, speed, grade)

    def _calculate_vo2(self, o2_cost_horiz: float, o2_cost_vert: float, speed: Speed, grade = 0.0) -> float:
        """Calculates the estimated VO2 reserve value.  The equation is:

        VO2 = (o2_cost_horiz x speed) + (o2_cost_vert x speed) + 3.5

        Where speed is expressed in meters/min.

        Args:
            o2_cost_horiz (float): Oxygen cost of moving each kg of bodyweight horizontally
            o2_cost_vert (float): Oxygen cost of moving each kg of bodyweight vertically
            speed (Speed): Speed the subject was moving at
            grade (float): Overall % grade of the surface an activity was performed on

        Returns:
            float: Estimated VO2 reserve value
        """
        meters_per_min = (speed.kph * 1000) / 60

        return (o2_cost_horiz * meters_per_min) + (o2_cost_vert * meters_per_min * grade) + 3.5

    def get_value(self) -> float:
        """Gets the estimated VO2 reserve value
        
        Returns:
            float: VO2 reserve value
        """
        return self._value

O2_COST_HORIZ_WALK = 0.1
"""float: Constant estimated oxygen cost of moving each kg of bodyweight horizontally while walking
"""

O2_COST_VERT_WALK = 1.8
"""float: Constant estimated oxygen cost of moving each kg of bodyweight vertically while walking
"""

O2_COST_HORIZ_RUN = 0.2
"""float: Constant estimated oxygen cost of moving each kg of bodyweight vertically while walking
"""

O2_COST_VERT_RUN = 0.9
"""float: Constant estimated oxygen cost of moving each kg of bodyweight horizontally while running
"""

def get_VO2(activity: activity.Activity, speed: Speed, grade = 0.0) -> VO2:
    """Factory method for instantiating a VO2 instance

    Args:
        activity (activity.Activity): Activity performed
        speed (Speed): Average speed of the activity
        grade (float): Percentage grade expressed as a decimal

    Returns:
        VO2: Instance of VO2 for the given activity

    Raises:
        Exception: If an invalid or unsupported activity is given as input
    """
    if activity.get_name() == 'walk':
        return VO2(o2_cost_horiz=O2_COST_HORIZ_WALK, o2_cost_vert=O2_COST_VERT_WALK, speed=speed, grade=grade)
    if activity.get_name() == 'run':
        return VO2(o2_cost_horiz=O2_COST_HORIZ_RUN, o2_cost_vert=O2_COST_VERT_RUN, speed=speed, grade=grade)

    raise Exception('Invalid or unsupported Activity')

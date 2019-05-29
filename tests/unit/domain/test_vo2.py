import pytest
from domain import activity, vo2
from measurement.measures import Speed

vo2_inst_testdata = [
    (0, 0, Speed(mph=0), 0, 3.5), # Should get resting constant value of 3.5
    (1, 1, Speed(kph=6), 0, 103.5),
    (vo2.O2_COST_HORIZ_RUN, vo2.O2_COST_VERT_RUN, Speed(kph=6), 0, 23.5),
    (vo2.O2_COST_HORIZ_WALK, vo2.O2_COST_VERT_WALK, Speed(mph=2), 0.15, 23.348576),
]

@pytest.mark.parametrize("o2_cost_horiz,o2_cost_vert,speed,grade,expected", vo2_inst_testdata)
def test_vo2_instantiation(o2_cost_horiz, o2_cost_vert, speed, grade, expected):
    vo2_est = vo2.VO2(
        o2_cost_horiz=o2_cost_horiz, 
        o2_cost_vert=o2_cost_vert, 
        speed=speed, 
        grade=grade
    )

    assert expected == vo2_est.get_value()

vo2_fact_testdata = [
    (activity.Run(), Speed(kph=6), 0, 23.5),
    (activity.Walk(), Speed(mph=2), 0.15, 23.348576),
]

@pytest.mark.parametrize("activity,speed,grade,expected_vo2_value", vo2_fact_testdata)
def test_vo2_factory_method(activity, speed, grade, expected_vo2_value):
    vo2_est = vo2.get_VO2(activity=activity, speed=speed, grade=grade)

    assert expected_vo2_value == vo2_est.get_value()

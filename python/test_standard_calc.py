from standard_calc import bound_to_180, is_angle_between

""" Tests for bound_to_180() """


def test_bound_basic1():
    # zero
    assert bound_to_180(0) == 0
    # between bounds
    assert bound_to_180(130) == 130
    assert bound_to_180(-130) == -130
    # endpoints
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180
    # not between bounds
    assert bound_to_180(200) == -160
    assert bound_to_180(-200) == 160
    # very large value
    assert bound_to_180(1230121) == 1


""" Tests for is_angle_between() """


def test_between_basic1():

    # between positive angles
    if is_angle_between(0, 1, 2):
        print("True!")
    # not between positive angles
    if not is_angle_between(0, 5, 2):
        print("False!")
    # between negative angles
    if is_angle_between(-10, -20, -30):
        print("True!")
    # not between very large angles
    if not is_angle_between(1234, -2342, 7898):
        print("False!")
    # with different signs
    if is_angle_between(170, -170, -160):
        print("True!")

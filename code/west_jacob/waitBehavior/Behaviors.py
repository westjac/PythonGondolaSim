def AdaptWait(peopleCount):  # GRADING: ADAPTING
    """
    Wait that changes depending on the number of people in the car.

    :param peopleCount: The number of people in the car.
    :return: 1.0 if peopleCount < 10
    :return: 2.0 if people count >= 10
    """
    if peopleCount < 10:
        return 1.0
    else:
        return 2.0


def ShortWait(peopleCount):  # GRADING: SMALL
    """
    Short wait time of 1.0 min

    :return: 1.0
    """
    return 1.0


def LongWait(peopleCount):  # GRADING: LARGE
    """
    Long wait of 2.0 minutes

    :return: 2.0
    """
    return 2.0

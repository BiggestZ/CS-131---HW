def cm_to_inches(cm):
    """Converts a measurement in centimeters to inches.

    This function should *print* out the equivalence, then *return* the result
    in inches. See example below. You should not round the argument or the
    parameter in any way.

    Note that one inch is exactly 2.54 centimeters.

    Args:
        cm (float): The measurement in centimeters. Must be non-negative.

    Returns:
        float: The measurement in inches.

    Examples:
        In this example, the function prints the line "2.54 cm is 1.0 inches",
        and returns 1.0. This is added to 63359 and printed, resulting in
        "63360.0".

        >>> print(63359 + cm_to_inches(2.54))
        2.54 cm is 1.0 inches
        63360.0

    """
    pass # FIXME delete this line when you are done


def can_go(red_light, turning_right, has_pedestrian):
    """Determine whether you can go through an intersection.

    This function determines whether you can go through an intersection under
    the given conditions. Keep in mind that in the US, you are allowed to turn
    right even if the traffic light is red (assuming no one is in the way and
    there is no sign prohibiting it).

    Args:
        red_light (bool): Whether there is a red light.
        turning_right (bool): Whether you are turning right.
        has_pedestrian (bool): Whether there is a pedestrian in the way.

    Returns:
        bool: True if you can go through an intersection under the given
            conditions; False otherwise.

    Examples:

        >>> print(can_go(True, True, False))
        True

        >>> print(can_go(False, False, True))
        False

    """
    pass # FIXME delete this line when you are done


def bio_to_age(bio):
    """Converts biographical-style information to an age.

    This function takes a string about a person, from a biography-like format:

        LAST, FIRST (BIRTH-DEATH)

    and converts it into a more natural age-based format

        FIRST LAST, AGE

    The death year optional; if no death year is present, assume the current
    year is 2018 to calculate the age. See examples below.

    Do not assume that names cannot contain spaces. Do not assume that years
    will have four digits.

    Args:
        bio (str): The biographical entry.

    Returns:
        str: The same information reformatted.

    Examples:

        >>> print(bio_to_age("Li, Justin (1982-)"))
        Justin Li, 35

        >>> print(bio_to_age("Clarke, Joan (1917-1996)"))
        Joan Clarke, 79

    """
    pass # FIXME delete this line when you are done


if __name__ == "__main__":
    """Test your functions here

    See textbook section 11.4 for an explanation of how this works.

  
    """
    print(63359 + cm_to_inches(2.54))

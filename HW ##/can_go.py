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
# Zahir Choudhry
# 10 / 5 / 2021
# CS 131 - HW #2

# If the Redlight is True

def can_go(r_l, t_r, has_pedestrian):
    if( r_l == False and has_pedestrian == False ): # No Redlight / No Pedestrian
        return True
    elif ( r_l == True and has_pedestrian == False and t_r == True ): # Right Turn/Redlight/No Pedestrian
        return True
    else:
        return False
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

print(can_go(True, True, False))
print()
print(can_go(False, False, True))
print()
print(can_go(False, False, False))
# print()
# print(can_go(False, True, False))
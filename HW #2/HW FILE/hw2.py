# Zahir Choudhry
# 10 / 5 / 2021
# HW #2 Part 1 - Cm to Inch

def cm_to_inches(cm):

    if (cm < 0): #Makes sure function only uses Non-Negative Numbers
        print("The vale input is negative. Please use non-negative numbers.")
        return None
    else:
        inch  = (cm / 2.54)
        print (str(cm) + " cm is " + str(inch) + " inches")
        return inch
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
pass

print(63359 + cm_to_inches(2.54))
print()
print(cm_to_inches(-2))



#__________________________________________________________________________________________________

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

# ___________________________________________________________________________________________________

# Zahir Choudhry
# 10 / 5 / 2021
# CS 131 HW #2 - bio_to_age

def bio_to_age(bio):
    last_name = ""
    first_name = ""
    place_holder = 0
    age = 0
    year1 = None
    year2 = None

    for i in range(len(bio)):
        if bio[i] == ",":
            place_holder = i+2
            last_name = bio[:i]
        # print(last_name)

        if bio[i] == "(":
            first_name = bio[place_holder:i-1]
            j = i+1
        # print(first_name)

        if bio[i] == "-":
            year1 = int(bio[j:i])
            j = i+1
            # print(year1)

        if bio[i] == ")":
            if bio[j:i].isnumeric():
                year2 = int(bio[j:i])
            # print(year2)
        # print(num_list)
    if (year2 == None ):
        age = 2018 - year1
    else:
        age = year2 - year1

    Final = first_name + " " + last_name + ", " + str(age)
    return Final
        # print(death_year - birth_year)

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

print(bio_to_age("Li, Justin (1982-)"))
print(bio_to_age("Clarke, Joan (1917-1996)"))
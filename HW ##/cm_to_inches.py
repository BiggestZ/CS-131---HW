def cm_to_inches(cm):
    print("XXXX")

    inch  = float(cm * 2.54)
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

print(cm_to_inches(2.54))


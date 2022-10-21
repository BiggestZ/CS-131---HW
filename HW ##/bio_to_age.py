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

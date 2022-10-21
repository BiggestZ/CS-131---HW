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
def power(number, pow=1):
    """Raise a number to the power of pow"""

    new_value = number ** pow
    return new_value


power(9, 2)
power(9, 1)
power(9) # Raises 9 to default argument of 1

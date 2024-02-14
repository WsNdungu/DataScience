def sqrt(x):
    """Returns the square of a number"""
    if x < 0:
        raise ValueError("x must be non-negative")

    try:
        return x ** 0.5

    except TypeError:
        print("x must be an int or a float")        


result = sqrt(16)
print(result)     
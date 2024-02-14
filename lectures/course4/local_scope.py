def square(value):

    """ Returns the square of a number """
    new_val = value ** 2
    return new_val
    
y = square(3)
print((y))
# new_val - Cannot be accessed here since it's defined as a local scope
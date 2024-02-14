new_val = 10

def square(value):
    """ Returns the square of a number """
    global new_val
    new_val = new_val ** 2
    return new_val
    
y = square(3)
print((y))

print(new_val)

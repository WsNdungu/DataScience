def raise_val(n):
    """Return the inner function."""
    
    def inner(x):
        """Raise x to the power of n."""
        raised = x ** n
        return raised
    
    return inner

square = raise_val(2)
cube = raise_val(3)

print(square(2), cube(4))

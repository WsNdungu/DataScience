def num_sequence(n):
    """ Generate values from 0 to n """

    i = 0
    while i < n:
        yield i
        i += 1

result = num_sequence(10)
print(result) 

# Iterate over the generator object
for item in result:
    print(item)

# List of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# List comprehension
fellow1 = [member for member in fellowship if len(member) >= 7]
print(type(fellow1))
print(fellow1)


# Generator expression
fellow2 = (member for member in fellowship if len(member) >= 7)
print(type(fellow2))
for member in fellow2:
    print(member)
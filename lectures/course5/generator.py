result = (2 ** num for num in range(10))

for num in result:
    print(num)

# create a list
result1 = (2 ** num for num in range(10))

print(list(result1))
print(next(result1))
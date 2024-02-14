# Old way
pairs_1 = []

for num1 in range(0, 2):
    for num2 in range(6, 8):
        pairs_1.append((num1, num2))

print(pairs_1)

# Using list comprehensions
pairs_2 = [(num1, num2) for num1 in range(0, 2) for num2 in range(6, 8)]
print(pairs_2)


# EX1

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
result2 = [doc[0] for doc in doctor]
print(result2)

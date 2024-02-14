# Iterable comprehensions
x = [num ** 2 for num in range(11) if num % 2 == 0]
print(x)

# Output comprehensions
y = [num ** 2 if num % 2 == 0 else 0 for num in range(11)]
print(y)

# Dictionary comprehensions
pos_neg_numbers = {num: -num for num in range(11)}
print(pos_neg_numbers)

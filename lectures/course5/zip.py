avengers = ["hawkeye", "iron man", "thor", "quicksilver"]
names = ["burton", "stark", "odinson", "maximoff"]

z = zip(avengers, names)
print(type((z)))

# Change the zip object into a list
z_list = list(z)
print(z_list) # Returns a list of tuples

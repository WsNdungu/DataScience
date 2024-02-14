# Create cookies list
cookies = ["chocolate chip", "peanut butter", "sugar"]
cookies.append("tirggel")
print(cookies)

# Create cakes list
cakes = ["strawberry", "vannila"]
print(cakes)

# Merge(concatenate) cookies list with cakes list using + operator
desserts = cookies + cakes
print(desserts)

# Locate an index of an element - index() method
position = cookies.index("sugar")
print(cookies)
print(cookies[3])

# Remove sugar from the list
name = cookies.pop(position)
print(cookies)

# Iterate over the list
for cookie in cookies:
    print(cookie)

# sort  the list - sorted()   
sorted_desserts = sorted(desserts)
print(sorted_desserts)
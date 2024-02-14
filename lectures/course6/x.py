# opening the file in read
with open('./data/baby_names.txt', 'r', newline='') as csvfile:
    

# Create the empty list: baby_names
baby_names = []

# Loop over records 
for row in records:
    # Add the name to the list
    baby_names.append(row[3])
# Sort the names in alphabetical order
for name in sorted(baby_names):
    # Print each name
    print(name)
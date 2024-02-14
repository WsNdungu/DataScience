import pandas as pd 
total = 0

for chunk in pd.read_csv("data/data.csv", chunksize=1000):
    # Append and calculate the sum of column x
    total += sum(chunk["Total Population"])

print((total)) 
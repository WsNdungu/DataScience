import pandas as pd 
result = []

for chunk in pd.read_csv("data/data.csv", chunksize=1000):
    # Append and calculate the sum of column x
    result.append(sum(chunk["Total Population"]))

total = sum(result) 
print((total))   
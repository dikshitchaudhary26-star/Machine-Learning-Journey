import pandas as pd

data = pd.read_csv("students.csv")

print(data)

print(data.head()) #by default 5

print(data.head(10))

print(data.tail()) 

print(data.describe())


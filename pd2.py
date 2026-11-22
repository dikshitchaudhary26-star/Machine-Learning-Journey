import pandas as pd

stu = {
    "name" : ["aarav","priya","rohit","isha"],
    "branch" : ["cse","it","cse","ece"],
    "marks" : [85,72,90,96],
}

df = pd.DataFrame(stu)

print(df)

print(df.shape)

print(df.dtypes)

#int 64 -> get converted to float64
#Int 64 -> nullable ignore nan

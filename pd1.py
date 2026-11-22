import pandas as pd

s = pd.Series([10,20,30,40],index = ['raj','anuj','ivana','aditya'])

print(s['raj'])
print(s)
print(s["raj"])
import numpy as np

a = np.arange(12).reshape(3,4)
print(a.mean(axis=0)) #across columns
print(a.mean(axis=1)) #across rows
print(a.mean())
print(a.std(axis=0))





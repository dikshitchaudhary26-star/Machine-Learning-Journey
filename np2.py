#by using numpy we can complete work fast
import numpy as np

import time

nums = list(range(1_000_000))

arr = np.arange(1_000_000)

t0 = time.time()

sum(nums)

print("list :",time.time() - t0)

t0 = time.time()

arr.sum()

print("Numpy :" , time.time() - t0)
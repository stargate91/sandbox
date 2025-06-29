import numpy as np

arr = np.random.rand(100)
_sum = np.sum(arr > 0.5)

_mean = np.mean(arr)
_med = np.median(arr)
_std = np.std(arr)


print("The 100 random numbers between 0 and 1: %s" % arr)
print("The number of numbers that are > 0.5: %s" %_sum)
print("The 100 random numbers' mean: %s" %_mean)
print("The 100 random numbers' median: %s"%_med)
print("The 100 random numbers' std: %s "%_std)
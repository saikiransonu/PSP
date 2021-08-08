import numpy as np

arr = np.empty((8,4))

for i in range(8):
    arr[i] = i
print(arr)

print(arr[[4,3,0,6]])
print(arr[[-3,-5,-7]])

arr = np.arange(32).reshape((8,4))
print(arr)
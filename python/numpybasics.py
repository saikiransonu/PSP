import numpy as np

my_arr = np.arange(10)
my_list = list(range(10))

print(my_arr)
print(my_list)

my_arr2 = my_arr*2
my_list2 = [x * 2 for x in my_list]

print(my_arr2)
print(my_list2)
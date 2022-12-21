# Write a Python program to compute element-wise sum of given tuples.
#         Original tuples: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
#         Element-wise sum of the said tuples: (6, 9, 8, 6) .  

my_tuple = (1, 2, 3, 4), (3, 5, 2, 1), (2, 2, 3, 1)
print(tuple(sum(x) for x in zip(*my_tuple)))
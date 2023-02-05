# Write a python script to find the repeated items of a tuple. tup=(1,2,2,3,4,4)

my_tuple = (1, 2, 2, 3, 4, 4)
print("Original tuple: ", my_tuple)
print(f"Repeated items:  {[x for x in my_tuple if my_tuple.count(x) > 1]}")

# Create a list a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a python program that prints out all the elements of the list that are less than 5

nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print([num for num in nums if num < 5])

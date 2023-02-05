# Write a Python program to unzip a list of tuples into individual lists.
# L= [(1,2), (3,4), (8,9)]

L = [(1, 2), (3, 4), (8, 9)]
for x in L:
    print(list(x))

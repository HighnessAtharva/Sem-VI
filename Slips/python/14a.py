# Write a Python program to convert a tuple of string values to a tuple of integer values.
# Original tuple values: (('44', '444'), ('1516', '45')) New tuple values: ((44, 444), (1516, 45))

print(tuple(tuple(map(int, i)) for i in (('44', '444'), ('1516', '45'))))

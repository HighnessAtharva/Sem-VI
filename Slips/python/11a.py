# Write a Python program that counts the number of occurrences of a character in a string.  

# Approach 1: Counter method (Would recommend)
from collections import Counter
my_string= 'thequickbrownfoxjumpsoverthelazydog'
print(Counter(my_string))

# Approach 2: Dictionary Comprehension (for dummies)
my_string= 'thequickbrownfoxjumpsoverthelazydog'
print({i:my_string.count(i) for i in my_string})

    

# Write a python program to accept string and remove the characters which have odd index values of given string using user defined function.

def remove_odd_index(text):
    print(text[::2])


remove_odd_index(input("Enter a string: "))

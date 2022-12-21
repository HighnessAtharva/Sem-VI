
# Write a python program to accept string and remove the characters which have odd index values of given string using user defined function. 



def remove_odd_index(text):
    return text[::2]

print(remove_odd_index("Hello World"))
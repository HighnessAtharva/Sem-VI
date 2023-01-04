
# Write a python program to accept string and remove the characters which have odd index values of given string using user defined function. 


# Atharva's solution
# def remove_odd_index(text):
#     return text[::2]

def remove_odd_index_chars(s):
    result = ""  # initialize an empty result string
    for i in range(len(s)):
        if i % 2 == 0:  # check if the index is even
            result += s[i]  # add the character to the result string
    return result

s = input("Enter a string: ")
print (remove_odd_index_chars(s))
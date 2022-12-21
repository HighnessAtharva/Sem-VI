# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.        

def count_upper_lower(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return f"Uppercase Characters: {upper}\nLower Characters: {lower}"

print(count_upper_lower("Hello World"))
print(count_upper_lower("I am a Python Developer!"))
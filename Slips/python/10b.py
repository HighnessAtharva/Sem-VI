# Write a python program to count number of upper case letters, small case letters, digits in the file. 

with open("10B-file.txt", "r", encoding='utf-8') as f:
    data = f.read()
    print(f"Data:\n{data}", end="\n=============\n")
    upper = 0
    lower = 0
    digit = 0
    for x in data:
        if x.isupper():
            upper += 1
        elif x.islower():
            lower += 1
        elif x.isdigit():
            digit += 1
    print(f"Upper case letters: {upper}")
    print(f"Lower case letters: {lower}")
    print(f"Digits: {digit}")
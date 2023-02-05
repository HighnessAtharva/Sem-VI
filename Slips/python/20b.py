# Write a python program to print the contents of file in reverse order

with open("20B-file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()[::-1]
    for line in lines:
        print(line)

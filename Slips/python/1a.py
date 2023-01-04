# 1.Write a Python program to print the following pattern.
# 1
# 2 3
# 4 5 6
# 7 8 9 10



n = 4  # number of rows

num = 1  # keeps track of the number to print
for i in range(n):
    # print the numbers for this row
    for j in range(i + 1):
        print(num, end=' ')
        num = num + 1
    print()  # move to the next line

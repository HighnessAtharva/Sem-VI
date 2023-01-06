# 1.Write a Python program to print the following pattern.
# 1
# 2 3
# 4 5 6
# 7 8 9 10


num = 1
for i in range(4):
    for _ in range(i+1):
        print(num, end=" ")
        num = num + 1
    print("\r")

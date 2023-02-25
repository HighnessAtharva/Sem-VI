# REPLACED SLIP QUESTION -> PREVIOUSLY: ARMSTRONG VALIDATION | UPDATED TO: PALINDROME VALIDATION

# Write a Python program to print whether a given number is Armstrong or not.

# def armstrong(num):
#     sum = 0
#     temp = num
#     while temp:
#         rem= temp % 10
#         sum +=rem ** 3
#         temp //= 10
#     return f"{num} is an armstrong number" if num == sum else f"{num} is not an armstrong number"

# print(armstrong(153))
# print(armstrong(154))


# ------------------------------
# PALINDROME VALIDATION
# ------------------------------

def palindrome(num):
    num=str(num)
    print(f"{num} is a palindrome" if num == num[::-1] else f"{num} is not a palindrome")

palindrome(1232)
palindrome(1221)
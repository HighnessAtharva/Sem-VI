# Write a Python program to print whether a given number is Armstrong or not.

def armstrong(num):
    sum = 0
    temp = num
    while temp:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return f"{num} is an armstrong number" if num == sum else f"{num} is not an armstrong number"


print(armstrong(153))
print(armstrong(154))

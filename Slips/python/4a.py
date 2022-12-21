# Write a Python Program to Check if given number is prime or not. Also find factorial of the given number using user defined function. 

def check_prime(N):
    # sourcery skip: remove-unreachable-code, use-next, useless-else-on-loop
    if N <= 1:
        return(f"{N} is not a prime number")
    for i in range(2, N):
        if (N % i) == 0:
            return(f"{N} is not a prime number")
            break
    else:
        return(f"{N} is a prime number")
    
    
def factorial(N):
    return 1 if N == 0 else N * factorial(N-1)


print(check_prime(7))
print(check_prime(6))
print(check_prime(13))
print("====================================")
print(f"Factorial of 5 is: {factorial(5)}")
print(f"Factorial of 0 is: {factorial(0)}")
print(f"Factorial of 6 is: {factorial(6)}")
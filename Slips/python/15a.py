# Write a Python program to accept two lists and merge the two lists into list of tuple.  

print(
    tuple(
        [int(input("Enter a number for list #1: ")) for _ in range(5)]
        + [int(input("Enter another number for list #2: ")) for _ in range(5)]
    )
)


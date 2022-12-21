# Write a Python program to accept n numbers in list and remove duplicates from a list.  

total_numbers = int(input("Enter total numbers: "))
my_list = [int(input("Enter number: ")) for _ in range(total_numbers)]
print(f"List with duplicates:  {my_list}")
print(f"List without duplicates: {list(set(my_list))}")
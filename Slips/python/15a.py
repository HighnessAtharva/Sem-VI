# Write a Python program to accept two lists and merge the two lists into list of tuple.  

l1 = [int(input(f"Enter {i+1}/{3} element for the list 1: ")) for i in range(3)]
l2 = [int(input(f"Enter {i+1}/{3} element for the list 2: ")) for i in range(3)]

l3 = []
l3.append(tuple(l1))
l3.append(tuple(l2))
print(l3)
# Write a python script to implement bubble sort using list.

def bubble_sort(list):
    for _ in range(len(list)):
        for j in range(len(list)-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


print("Sorted List:")
print(bubble_sort([9, 8, 1, 2, 3, 4, 6, 5, 10, 7]))

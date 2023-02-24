# Write a python script to implement bubble sort using list.

def bubble_sort(list):
    N= len(list)
    for i in range(N):
        for j in range(N-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


print("Sorted List:")
print(bubble_sort([9, 8, 1, 2, 3, 4, 6, 5, 10, 7]))

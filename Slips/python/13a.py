# REPLACED SLIP QUESTION -> PREVIOUSLY: BUBBLE SORT | UPDATED TO: SELECT SORT

# ------------------------------
# BUBBLE SORT
# ------------------------------

# def bubble_sort(list):
#     N= len(list)
#     for i in range(N):
#         for j in range(N-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]
#     return list

# print("Sorted List:")
# print(bubble_sort([9, 8, 1, 2, 3, 4, 6, 5, 10, 7]))


# ------------------------------
# SELECTION SORT
# ------------------------------
def selectionSort(a, n):
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            if a[i] < a[min_idx]:
                min_idx = i
        a[step], a[min_idx] = a[min_idx], a[step]

data = [-2, 45, 0, 11, -9]
n = len(data)
selectionSort(data, n)
print('Sorted Array in Ascending Order:')
print(data)
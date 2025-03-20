my_arr = [2, 4, 1, 5, 3]


# insertion sort
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            arr[j] = None
            j -= 1
        arr[j + 1] = key
    return arr


new_arr = insertion_sort(my_arr)
print(",".join(map(str, new_arr)))

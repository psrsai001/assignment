def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr


print(selection_sort([1, 9, 6, 4, 3]))

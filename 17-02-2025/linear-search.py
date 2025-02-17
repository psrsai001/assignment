def linear_search(arr, target):
    for ind, ele in enumerate(arr):
        if ele == target:
            return ind
    else:
        return -1

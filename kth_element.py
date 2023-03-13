import random
def quick_select(arr, start, end, k):
    print(end-start + 1)
    if start >= end:
        if start == end == k:
            return start
        return
    random_idx = random.randint(start, end)
    separator = partition(arr, start, end, random_idx)
    if separator == k:
        return separator
    elif separator < k:
        return quick_select(arr, separator+1, end, k)
    else:
        return quick_select(arr, start, separator-1, k)


def partition(arr, start, end, pivot_idx):
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    separator = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[separator] = arr[separator], arr[i]
            separator+=1

    arr[end], arr[separator] = arr[separator], arr[end]
    return separator





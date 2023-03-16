import random
import numpy as np


def quick_select_wrapper(arr, k):
    if k > len(arr) or k < 1:
        print("Error invalid value for K")
        return None
    return arr[quick_select(arr, 0, len(arr)-1, k-1)]
    


def quick_select(arr, start, end, k):
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




# arr = [-1 ,2 ,100, 4, 3, 1, 0, 20, 17]
# print(quick_select_wrapper(arr, 10))
# print(sorted(arr))
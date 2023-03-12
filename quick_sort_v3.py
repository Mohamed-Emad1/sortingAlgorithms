import random

def quicksort(arr, start, end):
    if end - start < 10:
        insertion_sort(arr, start, end)
        return

    # Median-of-three pivot selection
    mid = (start + end) // 2
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]

    pivot = arr[mid]
    left = start
    right = end - 1

    while True:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1

        if left >= right:
            break

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    arr[mid], arr[left] = arr[left], arr[mid]

    # Recurse on smaller subarrays first
    if left - start < end - left:
        quicksort(arr, start, left - 1)
        quicksort(arr, left + 1, end)
    else:
        quicksort(arr, left + 1, end)
        quicksort(arr, start, left - 1)


def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


import random

def quick_sort(arr, start, end):
    
    #Base case
    if start>=end:
        return
    
    #divide
    random_idx = random.randint(start, end)
    pivot = arr[random_idx]
    arr[random_idx], arr[end] = arr[end], arr[random_idx]
    separator = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[separator] = arr[separator], arr[i]
            separator+=1

    arr[end], arr[separator] = arr[separator], arr[end]



    #recursion
    quick_sort(arr, start, separator-1)
    quick_sort(arr, separator+1, end)
    return




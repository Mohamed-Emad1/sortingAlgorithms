import random


def quick_sort(arr, start, end):
    #Base case
    if start>=end:
        return 
    
    #divide
    random_idx = random.randint(start, end)
    pivot = arr[random_idx]
    separator = start
    for i in range(start, end+1):
        if arr[i] < pivot:
            arr[i], arr[separator] = arr[separator], arr[i]
            separator+=1

    #Check if array of duplicates
    if separator == start:
        first = arr[start]
        duplicates = True
        for i in range(start+1, end+1):
            if arr[i] != first:
                duplicates = False
                break
        if duplicates:
            return



    #recursion
    quick_sort(arr, start, separator-1)
    quick_sort(arr, separator, end)
    return 



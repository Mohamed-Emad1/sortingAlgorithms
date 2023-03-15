import time
import random


def insertionSort1(arr, n):  #####   insertionSort1 sort #########
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

    #####   end of insertionSort1 sort #########


def Selection_Sort(arr, n):  #####   Selection_Sort sort #########
    for i in range(0, n - 1):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr


#####  end of Selection_Sort sort #########

def heapify(arr, size, i):  #####   heap sort #########
    max = i
    left = (2 * i) + 1
    right = (2 * i) + 2

    if left < size and arr[max] < arr[left]:
        max = left  # take the max number
    if right < size and arr[max] < arr[right]:
        max = right
    if i != max:
        temp = arr[i]
        arr[i] = arr[max]
        arr[max] = temp
        heapify(arr, size, max)  ##build max heap after swap


def buildHeap(arr, n):
    i = int((n / 2) - 1)
    while i >= 0:
        heapify(arr, n, i)
        i -= 1


def heapSort(arr, n):
    buildHeap(arr, n)
    i = int((n - 1))
    while i >= 0:
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp  # swap first number and the last number
        heapify(arr, i, 0)  # build head again
        i -= 1

        #####   end of heap sort #########


def merge(arr, left, mid, right):  #####  merge sort #########
    leftLength = mid - left + 1
    rightLength = right - mid
    i = 0
    leftArr = arr[left:mid + 1]
    rightArr = arr[mid + 1:right + 1]

    # leftArr=[leftLength]
    # rightArr = [rightLength]
    # print(leftLength)

    # for i in range(0,leftLength+1):
    #     print(str(left)+"gdfgsf")
    #     print(i)
    #     leftArr[i] = arr[left+i]
    # for j in range(0,rightLength+1):
    #     rightArr[j] = arr[1+mid+j]

    k = left
    i = 0
    j = 0
    while i < leftLength and j < rightLength:  # comparison between left array and tight array when merging
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            k += 1
            i += 1

        else:
            arr[k] = rightArr[j]
            k += 1
            j += 1

    while i < leftLength:  # put all elements of the left array if the no elements left in the right array
        arr[k] = leftArr[i]
        k += 1
        i += 1

    while j < rightLength:  # put all elements of the left array if the no elements left in the right array
        arr[k] = rightArr[j]
        k += 1
        j += 1


def mergeSort(arr, left, right):
    if left < right:
        mid = (right + left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
    return arr


#####   end of merge sort #########

def hybird_merge_sort(arr, left, right, THRESHOLD):
    if right-left  > THRESHOLD:
        mid = (right + left) // 2
        hybird_merge_sort(arr, left, mid, THRESHOLD)
        hybird_merge_sort(arr, mid + 1, right, THRESHOLD)
        merge(arr, left, mid, right)
        return arr
    else:
        Selection_Sort(arr [left:right+1],right-left)


    # if  left+1 <right:
    #     mid = (right + left) // 2
    #         #return  Selection_Sort(arr , len(arr))
    #
    #     hybird_merge_sort(arr, left, mid, THRESHOLD)
    #     hybird_merge_sort(arr, mid + 1, right, THRESHOLD)
    #     merge(arr, left, mid, right)
    # else:
    #      print(Selection_Sort(arr[left:right + 1], len(arr[left:right + 1])))
    #
    # return arr

def main():

    arr = [random.randint(-1000, 1000) for i in range(0, 10000)]
    arrheap = [random.randint(-1000, 1000) for i in range(0, 100000)]
    arrSelct = [random.randint(-1000, 1000) for i in range(0, 550)]
    arrInsert = [random.randint(-1000, 1000) for i in range(0, 1000)]
    arrHyird = [random.randint(-1000, 1000) for i in range(0, 10000)]

    print("time for merge sort  = ", end="")  ##merge##
    # print(arr)
    start = time.time()
    mergeSort(arr, 0, len(arr) - 1)

    end = time.time()
    print("merge time = ", end="")
    print(end - start)

    print("-" * 70)

    start = time.time()
    heapSort(arrheap, len(arrheap))
    end = time.time()
    print("heap time = ", end="")
    print(end - start)

    print("-" * 70)

    start = time.time()
    Selection_Sort(arrSelct, len(arrSelct))
    end = time.time()
    print("selection time = ", end="")
    print(end - start)

    print("-" * 70)

    start = time.time()
    insertionSort1(arrInsert, len(arrInsert))
    end = time.time()
    print("Insertion time = ", end="")
    print(end - start)

    print("-" * 70)

    start = time.time()
    hybird_merge_sort(arrHyird, 0, len(arrHyird)- 1, 8)
    end = time.time()
    print("hypird merge time = ", end="")
    print(end - start)



if __name__ == "__main__":
    main()

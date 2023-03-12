def insertionSort1(arr, n):     #####   insertionSort1 sort #########
    for i in range(1,n):
        key = arr[i]
        j = i-1

        while j>=0 and arr[j]>key:
            arr[j+1] =arr[j]
            j-=1

        arr[j+1]=key
    return arr

    #####   end of insertionSort1 sort #########

def Selection_Sort(arr,n):   #####   Selection_Sort sort #########
    for i in range(0,n-1):
        min =  i
        for j in  range(i+1,n):
            if arr[j] < arr[min]:
               min = j
        if i != min:
            temp = arr[i]
            arr[i] = arr[min]
            arr[min] = temp
    return arr

#####  end of Selection_Sort sort #########

def heapify(arr,size,i):        #####   heap sort #########
    max = i
    left = (2*i)+1
    right = (2*i)+2

    if left<size and arr[max] < arr[left]:
        max =left                           # take the max number
    if right< size and arr[max] <arr[right]:
        max=right
    if i!=max:
        temp = arr[i]
        arr[i] = arr[max]
        arr[max] = temp
        heapify(arr,size,max)          ##build max heap after swap

def buildHeap(arr,n):
    i = int((n / 2) - 1)
    while i>=0:
        heapify(arr,n,i)
        i-=1



def heapSort(arr,n):
    buildHeap(arr,n)
    i=int((n-1))
    while i>=0:
        temp = arr[0]
        arr[0] = arr[i]
        arr[i] = temp            #swap first number and the last number
        heapify(arr,i,0)                #build head again
        i-=1

        #####   end of heap sort #########



def merge(arr,left,mid,right):               #####  merge sort #########
    leftLength = mid-left+1
    rightLength = right - mid
    i=0
    leftArr =arr[left:mid+1]
    rightArr = arr[mid+1:right+1]

    # leftArr=[leftLength]
    # rightArr = [rightLength]
    #print(leftLength)

    # for i in range(0,leftLength+1):
    #     print(str(left)+"gdfgsf")
    #     print(i)
    #     leftArr[i] = arr[left+i]
    # for j in range(0,rightLength+1):
    #     rightArr[j] = arr[1+mid+j]

    k =left
    i=0
    j=0
    while i < leftLength and j <rightLength:            # comparison between left array and tight array when merging
        if leftArr[i] <= rightArr[j]:
            arr[k] = leftArr[i]
            k += 1
            i += 1

        else:
            arr[k] = rightArr[j]
            k+=1
            j+=1

    while i<leftLength:         #put all elements of the left array if the no elements left in the right array
        arr[k] = leftArr[i]
        k+=1
        i+=1

    while j<rightLength:         #put all elements of the left array if the no elements left in the right array
        arr[k] = rightArr[j]
        k+=1
        j+=1

def mergeSort(arr,left,right):
    if left<right:
        mid = (right+left)//2
        mergeSort(arr, left, mid)
        mergeSort(arr,mid+1,right)
        merge(arr,left,mid,right)

 #####   end of merge sort #########

def hybird_merge_sort(arr,left,right,THRESHOLD):
    if left<right:
        mid = (right+left)//2
        if THRESHOLD==mid:
            Selection_Sort(arr,len(arr))
        else:
            hybird_merge_sort(arr, left, mid,THRESHOLD)
            hybird_merge_sort(arr,mid+1,right,THRESHOLD)
            merge(arr,left,mid,right)




arr = [100,3,6,9,-30,205,155]
arrheap = [100,3,6,9,-30,205,155]
arrSelct = [100,3,6,9,-30,205,155]
arrInsert = [100,3,6,9,-30,205,155]
arrHyird = [100,3,6,9,-30,205,155]


print("array before merge sort is = ",end="")       ##merge##
print(arr)
mergeSort(arr,0,len(arr)-1)
print("array after merge sort is = ",end="")
print(arr)

print("-"*70)

print("array before heap sort is = ",end="") ##HEAP##
print(arrheap)
(arrheap,len(arrheap))
print("array after heap sort is = ",end="")
print(arrheap)

print("-"*70)

print("array before Selection sort is = ",end="") ##Selct##
print(arrSelct)
Selection_Sort(arrSelct,len(arrSelct))
print("array after Selection sort is = ",end="")
print(arrSelct)

print("-"*70)

print("array before Insertion sort is = ",end="") ##insertionSort1##
print(arrInsert)
insertionSort1(arrInsert,len(arrInsert))
print("array after Insertion sort is = ",end="")
print(arrInsert)

print("-"*70)



print("-"*70)

print("array before Hybird merge sort  is = ",end="") ##insertionSort1##
print(arrHyird)
hybird_merge_sort(arrHyird,0,len(arrHyird)-1,2)
print("array after Hybird merge sort is = ",end="")
print(arrHyird)
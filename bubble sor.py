def Bubble_sort(arr,n):

    for i in range(0,n-1):
        flag = True
        for j in range(0,n-1-i):
            if arr[j] > arr[j+1]:
                flag=False
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        if flag == True:
            break
    return arr

arr =[10,5,3,90,177,-60]
print(Bubble_sort(arr,len(arr)))
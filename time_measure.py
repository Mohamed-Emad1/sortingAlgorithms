import numpy as np
import time 
import Sorting
import hybrid_test

def test_algorithms():
    array_sizes = [1000, 2000, 4000, 8000, 15_000, 25_000, 50_000, 100_000]
    min_val, max_val = -1000, 1000
    for array_size in array_sizes:
        print(f"With array of size {array_size}")
        random_arr = np.random.randint(min_val, max_val+1, size=(array_size,))

        #Merge Sort
        arr = random_arr.tolist()
        start_time = time.time()
        Sorting.mergeSort(arr, 0, array_size-1)
        print("Merge Sort: ", time.time() - start_time)

        #Quick Sort
        arr = random_arr.tolist()
        start_time = time.time()
        Sorting.quick_sort(arr, 0, array_size-1)
        print("Quick Sort: ", time.time() - start_time)

        #Heap Sort
        arr = random_arr.tolist()
        start_time = time.time()
        Sorting.heapSort(arr, array_size)
        print("Heap Sort: ", time.time() - start_time)

        #Insertion Sort
        arr = random_arr.tolist()
        start_time = time.time()
        Sorting.insertionSort1(arr, array_size)
        print("Insertion Sort: ", time.time() - start_time)


        #Selection Sort
        arr = random_arr.tolist()
        start_time = time.time()
        Sorting.Selection_Sort(arr, array_size)
        print("Selection Sort: ", time.time() - start_time)


        #Hybrid Sort
        arr = random_arr.tolist()
        start_time = time.time()
        hybrid_test.hybird_merge_sort(arr, 0, array_size-1, 5)
        print("Hybrid Sort: ", time.time() - start_time)

        print("\n\n\n")


if __name__ == "__main__":
    test_algorithms()



"""
With array of size 1000
Merge Sort:  0.02399754524230957
Quick Sort:  0.06400251388549805
Heap Sort:  0.023997068405151367
Insertion Sort:  0.33249831199645996
Selection Sort:  0.17005109786987305




With array of size 2000
Merge Sort:  0.04799985885620117
Quick Sort:  0.03200101852416992
Heap Sort:  0.06400370597839355
Insertion Sort:  0.7245159149169922
Selection Sort:  1.1599760055541992




With array of size 4000
Merge Sort:  0.15619850158691406
Quick Sort:  0.12480926513671875
Heap Sort:  0.17600250244140625
Insertion Sort:  3.420889139175415
Selection Sort:  2.3191895484924316




With array of size 8000
Merge Sort:  0.15404653549194336
Quick Sort:  0.10774040222167969
Heap Sort:  0.21855401992797852
Insertion Sort:  11.43311619758606
Selection Sort:  9.415617942810059




With array of size 15000
Merge Sort:  0.24808835983276367
Quick Sort:  0.2231290340423584
Heap Sort:  0.45505595207214355
Insertion Sort:  42.59434962272644
Selection Sort:  34.421101331710815




With array of size 25000
Merge Sort:  0.41287994384765625
Quick Sort:  0.3910655975341797
Heap Sort:  0.9615652561187744
Insertion Sort:  104.6897292137146
Selection Sort:  110.19692468643188




With array of size 50000
Merge Sort:  1.7504277229309082
Quick Sort:  1.5583794116973877
Heap Sort:  3.4236409664154053
Insertion Sort:  439.49827766418457
Selection Sort:  378.23344707489014




With array of size 100000
Merge Sort:  1.9489049911499023
Quick Sort:  1.9123148918151855
Heap Sort:  3.7285373210906982



"""
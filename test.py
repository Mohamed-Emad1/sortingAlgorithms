import numpy as np
import timeit


setup1 = """
import numpy as np
import quick_sort_v1
np.random.seed(7)
arr1 = np.random.randint(0, 10000, size=(50000,))
"""

setup2 = """
import numpy as np
import quick_sort_v2
np.random.seed(7)
arr2 = np.random.randint(0, 10000, size=(50000,))
"""


setup3 = """
import numpy as np
from Sorting import mergeSort
np.random.seed(7)
arr3 = np.random.randint(0, 10000, size=(50000,))
"""


setup4 = """
import numpy as np
import quick_sort_v3
np.random.seed(7)
arr4 = np.random.randint(0, 10000, size=(50000,))

"""

test1 = "quick_sort_v1.quick_sort(arr1, 0, len(arr1)-1)"


test2 = "quick_sort_v2.quick_sort(arr2, 0, len(arr2)-1)"

test3 = "mergeSort(arr3, 0, len(arr3)-1)"

test4 = "quick_sort_v3.quicksort(arr4, 0, len(arr4)-1)"

print("fixing a bug in the cmd")




print("Quick v1",timeit.timeit(stmt=test1, setup=setup1, number=1))
print("Quick v2",timeit.timeit(stmt=test2, setup=setup2, number=1))
print("Merge",timeit.timeit(stmt=test3, setup=setup3, number=1))
print("Quick v4",timeit.timeit(stmt=test4, setup=setup4, number=1))
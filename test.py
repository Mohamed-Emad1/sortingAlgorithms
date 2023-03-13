import numpy as np
import timeit


gen_arr = """
np.random.seed(7)
arr = np.random.randint(0, 10000, size=(300,))
"""


setup1 = """
import numpy as np
import quick_sort_v1
"""

setup2 = """
import numpy as np
import quick_sort_v2
"""


setup3 = """
import numpy as np
from Sorting import mergeSort
"""


setup4 = """
import numpy as np
import quick_sort_v3
"""

test1 = f"""
{gen_arr}
quick_sort_v1.quick_sort(arr, 0, len(arr)-1)
"""

test2 =f"""
{gen_arr}
quick_sort_v2.quick_sort(arr, 0, len(arr)-1)
"""

test3 =f"""
{gen_arr}
mergeSort(arr, 0, len(arr)-1)
"""

test4 = f"""
{gen_arr}
quick_sort_v3.quicksort(arr, 0, len(arr)-1)
"""

number = 1000
extra = timeit.timeit(stmt= gen_arr,setup=setup1, number=number)
v1 = timeit.timeit(stmt=test1, setup=setup1, number=number)
v2 = timeit.timeit(stmt=test2, setup=setup2, number=number)
v4 = timeit.timeit(stmt=test4, setup=setup4, number=number)

print((v1-extra)/number)
print((v2-extra)/number)
print((v4-extra)/number)

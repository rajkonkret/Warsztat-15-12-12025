import numpy as np
import tracemalloc

# The core of NumPy is well-optimized C code.
# Enjoy the flexibility of Python with the speed of compiled code.
#  pip install numpy

# numpy - biblioteka do działąń na tablicach i macierzach

tracemalloc.start()

# array1 = np.arange(10_000_000, dtype=np.int64)  # ndarray
# array1 = np.arange(10_000_000, dtype=np.int32)  # ndarray
array1 = np.arange(10_000_000, dtype=np.int8)  # ndarray
# array2 = np.arange(10_000_000, dtype=np.int64)
# array2 = np.arange(10_000_000, dtype=np.int32)
array2 = np.arange(10_000_000, dtype=np.int8)

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / 1024 ** 2} MB")
print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# Current memory usage: 152.5884552001953 MB
# Peak memory usage: 152.5884552001953 MB
# int64
# -------
# Current memory usage: 76.29450988769531 MB
# Peak memory usage: 76.29450988769531 MB
# int32
# --------
# Current memory usage: 19.074050903320312 MB
# Peak memory usage: 19.074050903320312 MB
# int8
print(np.iinfo(np.int64))
print(np.iinfo(np.int32))
print(np.iinfo(np.int8))
print(array1.dtype)  # wypisanie typu danych dla numpy
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
#
# Machine parameters for int32
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------
#
# Machine parameters for int8
# ---------------------------------------------------------------
# min = -128
# max = 127
# ---------------------------------------------------------------
#
# int8
# tracemalloc.start()

lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))

# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
# Current memory usage: 762.9212341308594 MB
# Peak memory usage: 762.9212341308594

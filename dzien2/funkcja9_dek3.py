import numpy as np
import tracemalloc
import time

# The core of NumPy is well-optimized C code.
# Enjoy the flexibility of Python with the speed of compiled code.
#  pip install numpy

# numpy - biblioteka do działąń na tablicach i macierzach

# tracemalloc.start()

# array1 = np.arange(10_000_000, dtype=np.int64)  # ndarray
# array1 = np.arange(10_000_000, dtype=np.int32)  # ndarray
array1 = np.arange(10_000_000, dtype=np.int8)  # ndarray
# array2 = np.arange(10_000_000, dtype=np.int64)
# array2 = np.arange(10_000_000, dtype=np.int32)
array2 = np.arange(10_000_000, dtype=np.int8)

# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB")
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
# print(np.iinfo(np.int64))
# print(np.iinfo(np.int32))
# print(np.iinfo(np.int8))
# print(array1.dtype)  # wypisanie typu danych dla numpy
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

def measure_time(func):
    def wrapper(*args, **kwargs):
        # start_time = time.time()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji: {func.__name__}: {execution_time}")
        return result

    return wrapper


@measure_time
def my_time():
    time.sleep(2)  # zatrzymuje program na 2 sekundy


@measure_time
def add_with_for():
    result = []
    for i in range(len(lista1)):
        suma = lista1[i] + lista2[i]
        result.append(suma)
    return "OK for"


@measure_time
def add_lc():
    result = [lista1[i] + lista2[i] for i in range(len(lista2))]
    return "Ok LC"


my_time()  # Czas wykonania funkcji: my_time: 2.0008054999634624
print(add_with_for())
print(add_lc())
# Czas wykonania funkcji: add_with_for: 1.486424500006251
# OK for
# Czas wykonania funkcji: add_lc: 1.2044600000372157
# Ok LC

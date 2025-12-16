import os
import psutil
# pip install psutil
import time

process = psutil.Process(os.getpid())


def rss_mb():
    return process.memory_info().rss / 1024 / 1024  # MB


before = rss_mb()
print(f"RSS before import: {before:.2f} MB")

import numpy
print(numpy.__version__)
time.sleep(1)

after = rss_mb()
print(f"RSS after import: {after:.2f} MB")
print(f"Delta: {after - before:.2f} MB")
# RSS before import: 33.96 MB
# RSS after import: 33.96 MB
# Delta: 0.00 MB

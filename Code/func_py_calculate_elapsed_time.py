# func_py_calculate_elapsed_time.py
from datetime import datetime

def func_py_calculate_elapsed_time(start, end):
    return end - start

start = datetime(2024, 1, 1, 12, 0)
end = datetime(2024, 1, 2, 12, 0)
print(func_py_calculate_elapsed_time(start, end))

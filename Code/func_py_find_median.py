# func_py_find_median.py
def func_py_find_median(lst):
    sorted_lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

print(func_py_find_median([12, 5, 8, 3, 10]))

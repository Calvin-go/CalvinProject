# func_py_find_second_largest.py
def func_py_find_second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.remove(max(unique_lst))
    return max(unique_lst)

print(func_py_find_second_largest([3, 1, 4, 1, 5, 9]))

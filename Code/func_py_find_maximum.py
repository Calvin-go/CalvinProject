# func_py_find_maximum.py
def func_py_find_maximum(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value

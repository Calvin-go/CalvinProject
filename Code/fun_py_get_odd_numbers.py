# fun_py_get_odd_numbers.py
def fun_py_get_odd_numbers(lst):
    return [i for i in lst if i % 2 != 0]

print(fun_py_get_odd_numbers([1, 2, 3, 4, 5, 6]))

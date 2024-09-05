# func_py_calculate_catalan_numbers.py
def func_py_calculate_catalan_numbers(n):
    if n == 0:
        return 1
    result = 0
    for i in range(n):
        result += func_py_calculate_catalan_numbers(i) * func_py_calculate_catalan_numbers(n - 1 - i)
    return result

print(func_py_calculate_catalan_numbers(5))

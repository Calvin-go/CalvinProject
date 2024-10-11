# func_py_factorial.py
def func_py_factorial(n):
    if n == 0:
        return 1
    return n * func_py_factorial(n-1)

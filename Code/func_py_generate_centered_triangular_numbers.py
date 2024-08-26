# func_py_generate_centered_triangular_numbers.py
def func_py_generate_centered_triangular_numbers(limit):
    return [3*n*(n-1)//2 + 1 for n in range(1, limit + 1)]

print(func_py_generate_centered_triangular_numbers(10))

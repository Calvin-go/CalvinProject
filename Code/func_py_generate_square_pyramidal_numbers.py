# func_py_generate_square_pyramidal_numbers.py
def func_py_generate_square_pyramidal_numbers(n):
    return [i * (i + 1) * (2 * i + 1) // 6 for i in range(1, n + 1)]

print(func_py_generate_square_pyramidal_numbers(10))

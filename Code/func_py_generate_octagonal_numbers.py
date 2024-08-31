# func_py_generate_octagonal_numbers.py
def func_py_generate_octagonal_numbers(limit):
    octagonal_numbers = [n * (3 * n - 2) for n in range(1, limit + 1)]
    return octagonal_numbers

print(func_py_generate_octagonal_numbers(10))

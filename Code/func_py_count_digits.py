# func_py_count_digits.py
def func_py_count_digits(string):
    return sum(1 for char in string if char.isdigit())

print(func_py_count_digits("Hello123"))

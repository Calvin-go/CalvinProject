# func_py_count_uppercase_letters.py
def func_py_count_uppercase_letters(string):
    return sum(1 for char in string if char.isupper())

print(func_py_count_uppercase_letters("Hello, World!"))

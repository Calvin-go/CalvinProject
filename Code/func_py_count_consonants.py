# func_py_count_consonants.py
def func_py_count_consonants(string):
    return sum(1 for char in string if char.lower() in 'bcdfghjklmnpqrstvwxyz')

print(func_py_count_consonants("Hello, World!"))

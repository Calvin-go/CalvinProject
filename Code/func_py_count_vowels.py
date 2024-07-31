# func_py_count_vowels.py
def func_py_count_vowels(string):
    vowels = 'aeiou'
    return sum(1 for char in string.lower() if char in vowels)

print(func_py_count_vowels("Hello, World!"))

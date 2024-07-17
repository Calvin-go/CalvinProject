# func_remove_vowels.py
def func_remove_vowels(string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in string if char not in vowels])

print(func_remove_vowels("Hello World"))

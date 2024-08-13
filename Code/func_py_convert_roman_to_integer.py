# func_py_convert_roman_to_integer.py
def func_py_convert_roman_to_integer(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    prev_value = 0
    for char in reversed(roman):
        value = roman_dict[char]
        if value < prev_value:
            integer -= value
        else:
            integer += value
        prev_value = value
    return integer

print(func_py_convert_roman_to_integer('XIV'))

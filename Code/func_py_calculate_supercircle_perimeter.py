# func_py_calculate_supercircle_perimeter.py
import math

def func_py_calculate_supercircle_perimeter(radius, p):
    return 4 * radius * math.pow(2, 1/p) * math.gamma(1 + 1/p) / math.gamma(1/p)

print(func_py_calculate_supercircle_perimeter(5, 2))

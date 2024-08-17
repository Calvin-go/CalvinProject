# func_py_calculate_oblate_spheroid_volume.py
import math

def func_py_calculate_oblate_spheroid_volume(radius1, radius2):
    return (4/3) * math.pi * radius1**2 * radius2

print(func_py_calculate_oblate_spheroid_volume(5, 3))

# func_py_calculate_dodecahedron_volume.py
import math

def func_py_calculate_dodecahedron_volume(edge_length):
    return (15 + 7 * math.sqrt(5)) / 4 * edge_length**3

print(func_py_calculate_dodecahedron_volume(3))

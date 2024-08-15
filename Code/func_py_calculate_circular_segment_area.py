# func_py_calculate_circular_segment_area.py
import math

def func_py_calculate_circular_segment_area(radius, angle):
    return 0.5 * radius**2 * (math.radians(angle) - math.sin(math.radians(angle)))

print(func_py_calculate_circular_segment_area(5, 60))

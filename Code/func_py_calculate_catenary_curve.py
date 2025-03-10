# func_py_calculate_catenary_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_catenary_curve(a, points):
    x = np.linspace(-10, 10, points)
    y = a * np.cosh(x / a)
    plt.plot(x, y)
    plt.title("Catenary Curve")
    plt.show()

func_py_calculate_catenary_curve(5, 1000)

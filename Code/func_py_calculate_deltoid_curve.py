# func_py_calculate_deltoid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_deltoid_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = 2 * a * np.cos(t) + a * np.cos(2 * t)
    y = 2 * a * np.sin(t) - a * np.sin(2 * t)
    plt.plot(x, y)
    plt.title("Deltoid Curve")
    plt.show()

func_py_calculate_deltoid_curve(5, 1000)

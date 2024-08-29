# func_py_calculate_cardioid_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_cardioid_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * (1 - np.cos(t)) * np.cos(t)
    y = a * (1 - np.cos(t)) * np.sin(t)
    plt.plot(x, y)
    plt.title("Cardioid Curve")
    plt.show()

func_py_calculate_cardioid_curve(5, 1000)

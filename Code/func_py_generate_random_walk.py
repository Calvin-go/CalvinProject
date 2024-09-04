# func_py_generate_random_walk.py
import matplotlib.pyplot as plt
import random

def func_py_generate_random_walk(steps):
    x, y = [0], [0]
    for _ in range(steps):
        angle = random.uniform(0, 2 * np.pi)
        x.append(x[-1] + np.cos(angle))
        y.append(y[-1] + np.sin(angle))
    plt.plot(x, y)
    plt.title("Random Walk")
    plt.show()

func_py_generate_random_walk(1000)

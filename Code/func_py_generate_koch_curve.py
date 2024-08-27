# func_py_generate_koch_curve.py
import turtle

def func_py_generate_koch_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        func_py_generate_koch_curve(length, depth - 1)
        turtle.left(60)
        func_py_generate_koch_curve(length, depth - 1)
        turtle.right(120)
        func_py_generate_koch_curve(length, depth - 1)
        turtle.left(60)
        func_py_generate_koch_curve(length, depth - 1)

turtle.speed("fastest")
func_py_generate_koch_curve(300, 4)
turtle.done()

# func_py_generate_fibonacci.py
def func_py_generate_fibonacci(n):
    if n <= 0:
        return []
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(func_py_generate_fibonacci(10))

# func_py_generate_self_numbers.py
def func_py_generate_self_numbers(limit):
    generated = set()
    for n in range(1, limit + 1):
        generated.add(n + sum(map(int, str(n))))
    self_numbers = [n for n in range(1, limit + 1) if n not in generated]
    return self_numbers

print(func_py_generate_self_numbers(100))

# func_py_generate_catalan_numbers.py
def func_py_generate_catalan_numbers(n):
    def factorial(x):
        return 1 if x == 0 else x * factorial(x - 1)
    
    return [factorial(2 * i) // (factorial(i + 1) * factorial(i)) for i in range(n)]

print(func_py_generate_catalan_numbers(10))

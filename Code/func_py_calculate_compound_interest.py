# func_py_calculate_compound_interest.py
def func_py_calculate_compound_interest(principal, rate, time):
    return principal * (1 + rate / 100) ** time

print(func_py_calculate_compound_interest(1000, 5, 2))

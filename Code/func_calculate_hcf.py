# func_calculate_hcf.py
def func_calculate_hcf(a, b):
    while b:
        a, b = b, a % b
    return a

print(func_calculate_hcf(48, 18))

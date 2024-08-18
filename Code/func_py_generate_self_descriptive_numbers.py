# func_py_generate_self_descriptive_numbers.py
def func_py_generate_self_descriptive_numbers(n):
    def is_self_descriptive(num):
        digits = str(num)
        return all(digits.count(str(i)) == int(digits[i]) for i in range(len(digits)))

    return [i for i in range(10**(n-1), 10**n) if is_self_descriptive(i)]

print(func_py_generate_self_descriptive_numbers(4))

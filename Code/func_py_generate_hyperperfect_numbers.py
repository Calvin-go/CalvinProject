# func_py_generate_hyperperfect_numbers.py
def func_py_generate_hyperperfect_numbers(k, limit):
    def is_hyperperfect(num):
        sum_divisors = sum(i for i in range(1, num) if num % i == 0)
        return num == k * (sum_divisors - 1) + 1

    return [i for i in range(2, limit) if is_hyperperfect(i)]

print(func_py_generate_hyperperfect_numbers(2, 100))

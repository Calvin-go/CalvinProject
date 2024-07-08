# 5. fun_is_prime.py
def fun_is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

print(fun_is_prime(29))
print(fun_is_prime(30))

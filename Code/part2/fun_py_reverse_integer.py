# fun_py_reverse_integer.py

def fun_py_reverse_integer(n):
    sign = -1 if n < 0 else 1
    return sign * int(str(abs(n))[::-1])

def test_reverse_integer():
    num = -12345
    print(f"Reversed integer: {fun_py_reverse_integer(num)}")

if __name__ == "__main__":
    test_reverse_integer()

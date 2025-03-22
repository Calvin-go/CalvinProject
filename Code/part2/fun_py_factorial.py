# fun_py_factorial.py

def fun_py_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fun_py_factorial(n - 1)

def test_factorial():
    number = 5
    print(f"Factorial of {number}: {fun_py_factorial(number)}")

if __name__ == "__main__":
    test_factorial()

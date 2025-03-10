# func_py_palindrome_checker.py
def func_py_palindrome_checker(s):
    clean_s = "".join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]

print(func_py_palindrome_checker("A man, a plan, a canal: Panama"))

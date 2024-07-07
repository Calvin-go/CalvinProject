# fun_is_palindrome.py
def fun_is_palindrome(string):
    return string == string[::-1]

print(fun_is_palindrome('racecar'))
print(fun_is_palindrome('hello'))

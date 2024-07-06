# fun_palindrome_checker.py
def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

string = "A man, a plan, a canal, Panama"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

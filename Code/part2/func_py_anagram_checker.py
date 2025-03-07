# func_py_anagram_checker.py
from collections import Counter

def func_py_anagram_checker(s1, s2):
    return Counter(s1.replace(" ", "").lower()) == Counter(s2.replace(" ", "").lower())

print(func_py_anagram_checker("listen", "silent"))

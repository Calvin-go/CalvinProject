# func_find_permutations.py
from itertools import permutations

def func_find_permutations(lst):
    return list(permutations(lst))

print(func_find_permutations([1, 2, 3]))

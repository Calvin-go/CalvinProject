# func_py_find_longest_words.py
def func_py_find_longest_word(words):
    return max(words, key=len)

print(func_py_find_longest_word(["hello", "world", "python", "programming"]))

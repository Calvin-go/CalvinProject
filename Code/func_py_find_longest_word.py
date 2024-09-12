# func_py_find_longest_word.py
def func_py_find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(func_py_find_longest_word("Python programming is amazing"))

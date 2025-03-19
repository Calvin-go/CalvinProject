# func_py_anagram.py

def func_py_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def test_anagram():
    print(f"Are 'listen' and 'silent' anagrams? {func_py_anagram('listen', 'silent')}")

if __name__ == "__main__":
    test_anagram()

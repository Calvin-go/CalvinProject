# fun_py_count_vowels.py

def fun_py_count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def test_count_vowels():
    words = ["hello", "programming", "beautiful"]
    for word in words:
        print(f"Vowel count in '{word}': {fun_py_count_vowels(word)}")

if __name__ == "__main__":
    test_count_vowels()

# func_py_vowel_count.py

def func_py_vowel_count(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def test_vowel_count():
    sentences = ["Hello World", "Python programming"]
    for s in sentences:
        print(f"Vowel count in '{s}': {func_py_vowel_count(s)}")

if __name__ == "__main__":
    test_vowel_count()

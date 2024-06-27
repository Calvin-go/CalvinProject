# calculate_word_count.py
def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    text = input("Enter a text: ")
    count = word_count(text)
    print(f"The number of words in the text is: {count}")

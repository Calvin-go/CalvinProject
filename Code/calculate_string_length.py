def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

def main():
    text = "Hello, World!"
    length = string_length(text)
    print(f"The length of the string '{text}' is: {length}")

if __name__ == "__main__":
    main()

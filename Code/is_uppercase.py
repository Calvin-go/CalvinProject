# is_uppercase.py
def is_uppercase(s):
    return s.isupper()

if __name__ == "__main__":
    s = input("Enter a string: ")
    if is_uppercase(s):
        print(f"{s} is in uppercase")
    else:
        print(f"{s} is not in uppercase")

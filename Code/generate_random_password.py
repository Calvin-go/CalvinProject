# generate_random_password.py
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Generated password: {password}")

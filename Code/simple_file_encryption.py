# simple_file_encryption.py
from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as file:
        file.write(decrypted)

if __name__ == "__main__":
    key = generate_key()
    file_path = 'test_file.txt'

    # Write a test file
    with open(file_path, 'w') as file:
        file.write("This is a test file for encryption and decryption.")

    encrypt_file(file_path,

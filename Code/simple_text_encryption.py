# simple_text_encryption.py
def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift value: "))
    encrypted_text = encrypt(text, shift)
    print(f"Encrypted text: {encrypted_text}")

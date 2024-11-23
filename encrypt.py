def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

def decrypt(text, shift):
    return encrypt(text, 26 - shift)
    
if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ")
    text = input("Enter your text: ")
    shift = int(input("Enter shift number: "))
    
    if choice == 'encrypt':
        print(f"Encrypted Text: {encrypt(text, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted Text: {decrypt(text, shift)}")

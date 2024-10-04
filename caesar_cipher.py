def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
     
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        encrypted_text = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_text}")
    elif choice == 'D':
        decrypted_text = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_text}")
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()

def caesar_cipher(text, shift):
    result = ''
    
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97  
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char 
    
    return result

text = input("Enter plain text: ")
shift = 3
encrypted_text = caesar_cipher(text, shift)
decrypted_text = caesar_cipher(encrypted_text, -shift)

print("Original text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)

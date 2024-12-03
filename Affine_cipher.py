def affine_encrypt(text, a, b):
    encrypted = ""
    for char in text.upper():
        if char.isalpha(): 
            x = ord(char) - 65 
            new_char = (a * x + b) % 26 
            encrypted += chr(new_char + 65) 
        else:
            encrypted += char 
    return encrypted

def affine_decrypt(cipher, a, b):
    decrypted = ""
    a_inverse = pow(a, -1, 26) 
    for char in cipher.upper():
        if char.isalpha():
            y = ord(char) - 65
            original_char = (a_inverse * (y - b)) % 26
            decrypted += chr(original_char + 65)
        else:
            decrypted += char
    return decrypted
msg=input("Enter the Plain Text: ")
# Example usage
a, b = 5, 8 # Keys
message = msg
cipher_text = affine_encrypt(message, a, b)
print("Encrypted:", cipher_text)
plain_text = affine_decrypt(cipher_text, a, b)
print("Decrypted:", plain_text)

import string

LETTERS = string.ascii_uppercase
SYMBOLS = "!@#$%^&*()_+[]{}|;:',.<>?/1234567890"
MAPPING = dict(zip(LETTERS, SYMBOLS))
REVERSE_MAPPING = {v: k for k, v in MAPPING.items()}

def substitution_encrypt(text):
    return ''.join(MAPPING.get(c, c) for c in text.upper())

def substitution_decrypt(cipher):
    return ''.join(REVERSE_MAPPING.get(c, c) for c in cipher)

msg = input("Enter the Plain Text: ")
cipher_text = substitution_encrypt(msg)
print("Encrypted:", cipher_text)
plain_text = substitution_decrypt(cipher_text)
print("Decrypted:", plain_text)

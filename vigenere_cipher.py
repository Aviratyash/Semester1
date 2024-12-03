def vigenere_encrypt(text, keyword):
    keyword = (keyword.upper() * ((len(text) // len(keyword)) + 1))[:len(text)]
    return ''.join(
        chr((ord(t.upper()) - 65 + ord(k) - 65) % 26 + 65) if t.isalpha() else t
        for t, k in zip(text, keyword)
    )

def vigenere_decrypt(cipher, keyword):
    keyword = (keyword.upper() * ((len(cipher) // len(keyword)) + 1))[:len(cipher)]
    return ''.join(
        chr((ord(c.upper()) - 65 - (ord(k) - 65) + 26) % 26 + 65) if c.isalpha() else c
        for c, k in zip(cipher, keyword)
    )

# Example usage
message = input("Enter the Plain Text: ")
keyword = input("Enter the Keyword: ")
cipher_text = vigenere_encrypt(message, keyword)
print("Encrypted:", cipher_text)
plain_text = vigenere_decrypt(cipher_text, keyword)
print("Decrypted:", plain_text)

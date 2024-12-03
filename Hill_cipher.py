import numpy as np
def text_to_int(text): 
    return [ord(c) - 65 for c in text.upper() if c.isalpha()]

def int_to_text(nums): 
    return ''.join(chr(n + 65) for n in nums)

def text_to_matrix(text, n):
    nums = text_to_int(text) + [0] * (n - len(text) % n)
    return np.array(nums).reshape(-1, n)

def mod_inverse(matrix, mod):
    det_inv = pow(int(np.round(np.linalg.det(matrix))) % mod, -1, mod)
    adj = np.round(np.linalg.inv(matrix) * np.linalg.det(matrix)).astype(int) % mod
    return (det_inv * adj) % mod

def hill_encrypt(plaintext, key_matrix):
    return int_to_text((np.dot(text_to_matrix(plaintext, key_matrix.shape[0]), key_matrix) % 26).flatten())

def hill_decrypt(ciphertext, key_matrix):
    decrypted_text = int_to_text((np.dot(text_to_matrix(ciphertext, key_matrix.shape[0]), mod_inverse(key_matrix, 26)) % 26).flatten())
    
    return decrypted_text.rstrip('A')

key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])

msg = input("Enter Plaintext: ")

cipher_text = hill_encrypt(msg, key_matrix)
print("Encrypted:", cipher_text)

plain_text = hill_decrypt(cipher_text, key_matrix)
print("Decrypted:", plain_text)

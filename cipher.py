def caesar_cipher_encrypt(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                ciphertext += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext


def caesar_cipher_decrypt(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr((ord(char) - 65 - key) % 26 + 65)
            else:
                plaintext += chr((ord(char) - 97 - key) % 26 + 97)
        else:
            plaintext += char
    return plaintext


# Example usage
plaintext = "Hello Poonam! How are you?"
key = 3

encrypted_text = caesar_cipher_encrypt(plaintext, key)
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)

print("Plaintext: ", plaintext)
print("Encrypted text: ", encrypted_text)
print("Decrypted text: ", decrypted_text)

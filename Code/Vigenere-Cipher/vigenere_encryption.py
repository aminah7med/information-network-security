
# Vigenere Encryption

plain = input("Enter the plain text: ").lower()
key = input("Enter the key: ").lower()

ciphertext = ""

for i in range(len(plain)):
    p = ord(plain[i]) - 97
    k = ord(key[i % len(key)]) - 97

    c = (p + k) % 26 + 97
    ciphertext += chr(c)

print("Ciphertext:", ciphertext)

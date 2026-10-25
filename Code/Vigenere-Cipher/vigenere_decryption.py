
# Vigenere Decryption

cipher = input("Enter the cipher text: ").lower()
key = input("Enter the key: ").lower()

plaintext = ""

for i in range(len(cipher)):
    c = ord(cipher[i]) - 97
    k = ord(key[i % len(key)]) - 97

    p = (c - k) % 26 + 97
    plaintext += chr(p)

print("Plaintext:", plaintext)


# Caesar Encryption

plaintext = input("Enter the plaintext: ").upper()
key = int(input("Enter the key: "))

ciphertext = ""

for i in plaintext:
    if i.isalpha():
        p = ord(i) - 65
        c = (p + key) % 26 + 65
        ciphertext += chr(c)
    else:
        ciphertext += i

print("Ciphertext:", ciphertext)

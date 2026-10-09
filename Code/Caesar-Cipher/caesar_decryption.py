
# Caesar Decryption

ciphertext = input("Enter the ciphertext: ").upper()
key = int(input("Enter the key: "))

plaintext = ""

for i in ciphertext:
    if i.isalpha():
        c = ord(i) - 65
        p = (c - key) % 26 + 65
        plaintext += chr(p)
    else:
        plaintext += i

print("Plaintext:", plaintext)

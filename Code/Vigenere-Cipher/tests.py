
# Vigenere Cipher Tests

# Test 1: Encryption
plain = "cat"
key = "dog"

ciphertext = ""

for i in range(len(plain)):
    p = ord(plain[i]) - 97
    k = ord(key[i % len(key)]) - 97
    c = (p + k) % 26 + 97
    ciphertext += chr(c)

print("Test 1 - Expected: foz")
print("Test 1 - Actual:  ", ciphertext)
print("Passed:", ciphertext == "foz")


# Test 2: Decryption
plaintext = ""

for i in range(len(ciphertext)):
    c = ord(ciphertext[i]) - 97
    k = ord(key[i % len(key)]) - 97
    p = (c - k) % 26 + 97
    plaintext += chr(p)

print("\nTest 2 - Expected: cat")
print("Test 2 - Actual:  ", plaintext)
print("Passed:", plaintext == "cat")


# Test 3: Key Repetition
plain = "hello"
key = "key"

new_key = ""

for i in range(len(plain)):
    new_key += key[i % len(key)]

print("\nTest 3 - Expected: keyke")
print("Test 3 - Actual:  ", new_key)
print("Passed:", new_key == "keyke")


# Caesar Cipher Tests

# Test 1: Encryption
plaintext = "OMAR"
key = 5

ciphertext = ""

for i in plaintext:
    p = ord(i) - 65
    c = (p + key) % 26 + 65
    ciphertext += chr(c)

print("Test 1 - Expected: TRFW")
print("Test 1 - Actual:  ", ciphertext)
print("Passed:", ciphertext == "TRFW")

# Test 2: Decryption
plaintext = ""

for i in ciphertext:
    c = ord(i) - 65
    p = (c - key) % 26 + 65
    plaintext += chr(p)

print("\nTest 2 - Expected: OMAR")
print("Test 2 - Actual:  ", plaintext)
print("Passed:", plaintext == "OMAR")

# Test 3: Wrap around the alphabet
plaintext = "XYZ"
key = 3

ciphertext = ""

for i in plaintext:
    p = ord(i) - 65
    c = (p + key) % 26 + 65
    ciphertext += chr(c)

print("\nTest 3 - Expected: ABC")
print("Test 3 - Actual:  ", ciphertext)
print("Passed:", ciphertext == "ABC")

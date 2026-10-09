# Instructor's section code (reference implementation).
# Assumes: lowercase ASCII letters only (a-z) and a non-empty key.

plain = input("Enter the plain text: ")
key = input("Enter the key: ")

new_plain = ""      # stores the repeated key (name kept from the lecture code)
ciphertext = ""

for i in range(len(plain)):
    new_plain += key[i % len(key)]

    p = ord(plain[i]) - 97
    k = ord(new_plain[i]) - 97

    c = ((p + k) % 26) + 97
    ciphertext += chr(c)

print("Ciphertext:", ciphertext)

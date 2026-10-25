plain = input("Enter the original text: ").upper()
key = input("Enter the key: ").upper()

cipher = ""
new_key = ""



for i in range(len(plain)):

    new_key += key[i % len(key)]
    p = ord(plain[i]) - 65
    k = ord(new_key[i]) - 65
    c = ((p + k) % 26) + 65

    cipher += chr(c)


print("Plain Text :", plain)
print("Key        :", key)
print("Cipher Text:", cipher)

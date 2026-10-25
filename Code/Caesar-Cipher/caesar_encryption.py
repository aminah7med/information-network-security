plain = input("Enter the original text: ").upper()
key = int(input("Enter the key: "))


cipher = ""

for char in plain:
    if char.isalpha():
        p = ord(char) - 65
        c = (p + key) % 26
        cipher += chr(c + 65)
    else:
        cipher += char

print("Plain Text  :", plain)
print("Cipher Text :", cipher)
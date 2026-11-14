"""create a key matrix that used in encryption operation """
n = int(input('enter no of dimension'))
key = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input('enter value')))
        #l.append(random.randint(0,25))
    key.append(l)
print(key)
plain = input('enter plaintext')
plain = plain.upper()
ciphertext = ""
for i in range(0, len(plain), n):
    l = []
    for j in range(i, i + n):
        p = ord(plain[j]) - 65
        l.append(p)
    print(l)
    """" multiply two matrices"""
    for j in range(n):
        sum = 0
        for i in range(n):
            sum += key[j][i] * l[i]
        sum = chr((sum % 26) + 65)
        ciphertext += sum
print(ciphertext)

import random
hill_enc("asma",2)
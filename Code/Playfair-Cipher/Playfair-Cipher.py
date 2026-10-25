Alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def Search(Matrix, ch):
    for r in range(5):
        for c in range(5):
            if Matrix[r][c] == ch:
                return r, c


Plain = input("plaintext: ").upper().replace("J", "I").replace(" ", "")
Key = input("key: ").upper().replace("J", "I").replace(" ", "")

Mat = []
for i in Key:
    if i not in Mat:
        Mat.append(i)
for i in Alpha:
    if i not in Mat:
        Mat.append(i)
print(Mat)

Matrix = []
for i in range(0, 25, 5):
    Matrix.append(Mat[i:i + 5])
print(Matrix)

# build new_p: split into pairs, X between double letters, X at the end if odd
new_p = ""
i = 0
while i < len(Plain):
    a = Plain[i]
    if i + 1 < len(Plain):
        b = Plain[i + 1]
    else:
        b = "X"
    if a == b:
        new_p += a + "X"
        i += 1
    else:
        new_p += a + b
        i += 2
print("new_p =", new_p)

Cipher = ""
for i in range(0, len(new_p), 2):
    a = new_p[i]
    b = new_p[i + 1]

    r1, c1 = Search(Matrix, a)
    r2, c2 = Search(Matrix, b)

    if r1 == r2:
        Cipher += Matrix[r1][(c1 + 1) % 5]
        Cipher += Matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        Cipher += Matrix[(r1 + 1) % 5][c1]
        Cipher += Matrix[(r2 + 1) % 5][c2]
    else:
        Cipher += Matrix[r1][c2]
        Cipher += Matrix[r2][c1]

print("Cipher =", Cipher)

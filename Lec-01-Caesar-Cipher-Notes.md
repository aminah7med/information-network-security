# Information & Network Security --- Lecture 01

## 📌 Topic

**Introduction to Information Security & Classical Encryption --- Caesar
Cipher**

------------------------------------------------------------------------

## 1. 🔐 Basic Encryption Concepts

### Plaintext

The original readable message before encryption.

### Encryption

The process of transforming the **Plaintext** into an unreadable form.

### Ciphertext

The encrypted message produced after encryption.

### Decryption

The process of transforming the **Ciphertext** back into the original
**Plaintext**.

``` text
Plaintext
    ↓
 Encryption
    ↓
Ciphertext
    ↓
 Decryption
    ↓
Plaintext
```

------------------------------------------------------------------------

## 2. 🔑 Encryption Techniques

### Symmetric Encryption

-   Uses **one key**.
-   The same key is used for the encryption/decryption process.
-   The lecture introduces two classical techniques under this idea:
    -   **Substitution**
    -   **Transposition**

### Asymmetric Encryption

-   Uses **two keys**.
-   **Public Key**
-   **Private Key**
-   **RSA** is mentioned as an example.

------------------------------------------------------------------------

## 3. Classical Encryption

### Substitution

The characters are replaced by other characters.

``` text
Example idea:
AMIN → ROMA
```

The important idea is that the characters are **substituted**.

### Transposition

The characters themselves remain the same, but their **order is
changed**.

``` text
Example idea:
ROMA → ORMA
```

The important idea is that the same characters are rearranged.

------------------------------------------------------------------------

# 4. 🔄 Caesar Cipher

The Caesar Cipher is introduced in the lecture as a simple classical
encryption algorithm.

### Main Idea

Each character is shifted by a fixed number of positions in the
alphabet.

The fixed number is the **Key**.

``` text
Key = 5
```

For the alphabet, the lecture uses:

``` text
A = 0
B = 1
C = 2
...
Z = 25
```

So we work with **26 letters**.

------------------------------------------------------------------------

## 5. 📐 Caesar Encryption Formula

``` text
C = (P + K) % 26
```

Where:

-   `P` = Plaintext character index
-   `K` = Key
-   `C` = Ciphertext character index
-   `% 26` = keeps the result inside the range `0–25`

### Decryption Formula

``` text
P = (C - K) % 26
```

This moves the character backward by the same key.

------------------------------------------------------------------------

# 6. 🧮 Example 1 --- Single Character

### Given

``` text
Plaintext = O
Key = 5
```

Using:

``` text
A = 0
B = 1
...
O = 14
```

Apply the formula:

``` text
C = (P + K) % 26

C = (14 + 5) % 26
C = 19
```

Index `19` is:

``` text
T
```

### Result

``` text
O → T
```

------------------------------------------------------------------------

# 7. 🧮 Example 2 --- OMAR with Key = 5

### Given

``` text
Plaintext = OMAR
Key = 5
```

Convert every character to its index:

``` text
O = 14
M = 12
A = 0
R = 17
```

Apply:

``` text
C = (P + K) % 26
```

### O

``` text
(14 + 5) % 26 = 19 → T
```

### M

``` text
(12 + 5) % 26 = 17 → R
```

### A

``` text
(0 + 5) % 26 = 5 → F
```

### R

``` text
(17 + 5) % 26 = 22 → W
```

### Ciphertext

``` text
OMAR → TRFW
```

------------------------------------------------------------------------

# 8. 🧮 Example 3 --- ABC with Key = 3

### Given

``` text
Plaintext = ABC
Key = 3
```

``` text
A = 0 → (0 + 3) % 26 = 3 → D
B = 1 → (1 + 3) % 26 = 4 → E
C = 2 → (2 + 3) % 26 = 5 → F
```

### Result

``` text
ABC → DEF
```

------------------------------------------------------------------------

# 9. 🧮 Example 4 --- XYZ with Key = 3

This example shows why we need `% 26`.

### X

``` text
X = 23

(23 + 3) % 26
= 26 % 26
= 0
→ A
```

### Y

``` text
Y = 24

(24 + 3) % 26
= 27 % 26
= 1
→ B
```

### Z

``` text
Z = 25

(25 + 3) % 26
= 28 % 26
= 2
→ C
```

### Result

``` text
XYZ → ABC
```

The `% 26` operation makes the alphabet **wrap around** after `Z`.

------------------------------------------------------------------------

# 10. 🔓 Example 5 --- Decryption

Suppose:

``` text
Ciphertext = TRFW
Key = 5
```

Use:

``` text
P = (C - K) % 26
```

### T

``` text
T = 19

(19 - 5) % 26
= 14
→ O
```

### R

``` text
R = 17

(17 - 5) % 26
= 12
→ M
```

### F

``` text
F = 5

(5 - 5) % 26
= 0
→ A
```

### W

``` text
W = 22

(22 - 5) % 26
= 17
→ R
```

### Result

``` text
TRFW → OMAR
```

So encryption and decryption are opposite operations:

``` text
Encryption:
P → C
(P + K) % 26

Decryption:
C → P
(C - K) % 26
```

------------------------------------------------------------------------

# 11. 🧠 Quick Summary

  Concept         Meaning
  --------------- ---------------------------------------
  Plaintext       Original readable message
  Encryption      Converts plaintext to ciphertext
  Ciphertext      Encrypted message
  Decryption      Converts ciphertext back to plaintext
  Symmetric       Uses one key
  Asymmetric      Uses two keys
  Public Key      One of the asymmetric keys
  Private Key     One of the asymmetric keys
  Substitution    Replaces characters
  Transposition   Rearranges characters
  Caesar Cipher   Shifts characters by a fixed key

------------------------------------------------------------------------

## 🎯 Caesar Cipher Checklist

When solving a Caesar Cipher problem:

1.  Write the alphabet indexes from `0` to `25`.
2.  Identify the **Plaintext**.
3.  Identify the **Key**.
4.  Convert each character to its index.
5.  For encryption, use:

``` text
C = (P + K) % 26
```

6.  Convert the resulting index back to a character.
7.  Repeat for every character.
8.  For decryption, use:

``` text
P = (C - K) % 26
```

------------------------------------------------------------------------

## 💡 Important Notes

-   Caesar Cipher works **character by character**.
-   The key is a **number**.
-   The alphabet is represented using indexes `0–25`.
-   `% 26` handles the wrap-around from `Z` back to `A`.
-   The lecture presents Caesar as a simple classical encryption
    algorithm.
-   The examples above follow the notation and approach used in the
    lecture notes.

------------------------------------------------------------------------

## 📚 Lecture Progress

-   [x](#x) Encryption & Decryption
-   [x](#x) Plaintext & Ciphertext
-   [x](#x) Symmetric Encryption
-   [x](#x) Asymmetric Encryption
-   [x](#x) Public Key & Private Key
-   [x](#x) Substitution
-   [x](#x) Transposition
-   [x](#x) Caesar Cipher
-   [x](#x) Caesar Encryption Formula
-   [x](#x) Caesar Decryption Formula
-   [x](#x) Practice Examples

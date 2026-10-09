"""Supplementary practice implementation: Vigenere decryption.

Not the instructor's original code. Same convention as the lecture code
(a = 0 ... z = 25, lowercase letters only).

Formula: P_i = (C_i - K_i) mod 26

Python's % operator returns a value from 0 to 25 for a positive modulus,
so a negative difference such as -3 becomes 23. Other languages (C, C++,
C#, Java, JavaScript) can return a negative value; use ((x % 26) + 26) % 26
there.
"""


def decrypt(cipher, key):
    """Return the plaintext of `cipher` using `key` (lowercase a-z only)."""
    if not key:
        raise ValueError("The key must not be empty.")
    if not all("a" <= ch <= "z" for ch in key):
        raise ValueError("The key must contain lowercase letters a-z only.")
    if not all("a" <= ch <= "z" for ch in cipher):
        raise ValueError("The ciphertext must contain lowercase letters a-z only.")

    plaintext = ""
    for i in range(len(cipher)):
        c = ord(cipher[i]) - 97
        k = ord(key[i % len(key)]) - 97
        p = (c - k) % 26
        plaintext += chr(p + 97)
    return plaintext


if __name__ == "__main__":
    cipher = input("Enter the cipher text: ")
    key = input("Enter the key: ")
    print("Plaintext:", decrypt(cipher, key))

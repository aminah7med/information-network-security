"""Supplementary practice implementation: Vigenere encryption.

Not the instructor's original code. It uses the same convention as the
lecture code (a = 0 ... z = 25, lowercase letters only) and wraps the logic
in a function so it can be tested.

Formula: C_i = (P_i + K_i) mod 26
"""


def _is_lowercase_letters(text):
    """True if every character is a lowercase ASCII letter a-z."""
    return all("a" <= ch <= "z" for ch in text)


def encrypt(plain, key):
    """Return the ciphertext of `plain` using `key` (lowercase a-z only)."""
    if not key:
        raise ValueError("The key must not be empty.")
    if not _is_lowercase_letters(key):
        raise ValueError("The key must contain lowercase letters a-z only.")
    if plain != "" and not _is_lowercase_letters(plain):
        raise ValueError("The plaintext must contain lowercase letters a-z only.")

    ciphertext = ""
    for i in range(len(plain)):
        p = ord(plain[i]) - 97
        k = ord(key[i % len(key)]) - 97
        c = (p + k) % 26
        ciphertext += chr(c + 97)
    return ciphertext


if __name__ == "__main__":
    plain = input("Enter the plain text: ")
    key = input("Enter the key: ")
    print("Ciphertext:", encrypt(plain, key))

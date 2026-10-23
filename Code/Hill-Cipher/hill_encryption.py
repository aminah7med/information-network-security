"""Hill Cipher encryption using A = 0 through Z = 25."""

from math import gcd


MODULUS = 26


def validate_key_matrix(key_matrix):
    """Return the matrix dimension or raise ValueError for an invalid key."""
    if not isinstance(key_matrix, (list, tuple)) or not key_matrix:
        raise ValueError("Key matrix must be a non-empty square matrix.")

    dimension = len(key_matrix)
    if any(
        not isinstance(row, (list, tuple)) or len(row) != dimension
        for row in key_matrix
    ):
        raise ValueError("Key matrix must be square.")

    for row in key_matrix:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("Key matrix entries must be integers from 0 to 25.")
            if not 0 <= value < MODULUS:
                raise ValueError("Key matrix entries must be integers from 0 to 25.")

    return dimension


def normalize_text(text, label):
    """Convert ASCII letters to uppercase and reject unsupported characters."""
    if not isinstance(text, str):
        raise ValueError(f"{label} must be a string.")

    normalized = text.upper()
    if any(not "A" <= character <= "Z" for character in normalized):
        raise ValueError(f"{label} must contain only English letters A through Z.")

    return normalized


def encrypt(plaintext, key_matrix):
    """Encrypt letters in blocks, padding the final block with X if needed."""
    dimension = validate_key_matrix(key_matrix)
    plaintext = normalize_text(plaintext, "Plaintext")
    padding_length = (-len(plaintext)) % dimension
    plaintext += "X" * padding_length

    ciphertext = []
    for start in range(0, len(plaintext), dimension):
        block = [ord(letter) - ord("A") for letter in plaintext[start:start + dimension]]
        for row in key_matrix:
            value = sum(key_value * letter for key_value, letter in zip(row, block))
            ciphertext.append(chr((value % MODULUS) + ord("A")))

    return "".join(ciphertext)


def read_key_matrix():
    """Read a square key matrix from semicolon-separated, comma-separated rows."""
    rows = input("Enter key matrix rows (for example, 3,3;2,5): ").split(";")
    try:
        key_matrix = [
            [int(value.strip()) for value in row.split(",")]
            for row in rows
        ]
    except ValueError as error:
        raise ValueError("Key matrix must contain comma-separated integers.") from error

    validate_key_matrix(key_matrix)
    return key_matrix


if __name__ == "__main__":
    try:
        message = input("Enter the plaintext (English letters only): ")
        key = read_key_matrix()
        print("Ciphertext:", encrypt(message, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

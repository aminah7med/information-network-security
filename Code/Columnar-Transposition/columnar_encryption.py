"""Columnar Transposition Cipher encryption."""


def validate_key(key):
    """Return a valid key as a list of distinct positive integers."""
    if not isinstance(key, (list, tuple)) or not key:
        raise ValueError("Key must be a non-empty sequence of positive integers.")

    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in key
    ):
        raise ValueError("Key values must be positive integers.")

    if len(set(key)) != len(key):
        raise ValueError("Key values must be distinct.")

    return list(key)


def read_key():
    """Read key values separated by spaces."""
    try:
        key = [int(value) for value in input("Enter the numerical key: ").split()]
    except ValueError as error:
        raise ValueError("Key must contain space-separated integers.") from error

    return validate_key(key)


def encrypt(plaintext, key):
    """Write normalized plaintext in rows and read columns by key order."""
    key = validate_key(key)
    if not isinstance(plaintext, str):
        raise ValueError("Plaintext must be a string.")

    plaintext = "".join(plaintext.split())
    column_count = len(key)
    grid = [
        list(plaintext[start:start + column_count])
        for start in range(0, len(plaintext), column_count)
    ]
    column_order = sorted(range(column_count), key=lambda column: key[column])

    ciphertext = []
    for column in column_order:
        for row in grid:
            if column < len(row):
                ciphertext.append(row[column])

    return "".join(ciphertext)


if __name__ == "__main__":
    try:
        plaintext = input("Enter the plaintext: ")
        key = read_key()
        print("Ciphertext:", encrypt(plaintext, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

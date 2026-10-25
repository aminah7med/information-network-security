"""Columnar Transposition Cipher decryption."""

from columnar_encryption_supplementary import read_key, validate_key


def decrypt(ciphertext, key):
    """Restore columns by key order, then read the grid row by row."""
    key = validate_key(key)
    if not isinstance(ciphertext, str):
        raise ValueError("Ciphertext must be a string.")

    ciphertext = "".join(ciphertext.split())
    column_count = len(key)
    full_rows, extra_characters = divmod(len(ciphertext), column_count)
    column_order = sorted(range(column_count), key=lambda column: key[column])

    # The incomplete last row fills its leftmost columns first.
    grid_columns = [[] for _ in range(column_count)]
    position = 0
    for column in column_order:
        column_length = full_rows
        if column < extra_characters:
            column_length += 1
        grid_columns[column] = list(ciphertext[position:position + column_length])
        position += column_length

    plaintext = []
    for row in range(full_rows + (1 if extra_characters else 0)):
        for column in range(column_count):
            if row < len(grid_columns[column]):
                plaintext.append(grid_columns[column][row])

    return "".join(plaintext)


if __name__ == "__main__":
    try:
        ciphertext = input("Enter the ciphertext: ")
        key = read_key()
        print("Plaintext:", decrypt(ciphertext, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

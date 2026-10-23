"""Rail Fence Cipher encryption."""


def validate_key(key):
    """Ensure the number of rails is a positive integer."""
    if isinstance(key, bool) or not isinstance(key, int) or key <= 0:
        raise ValueError("Key must be a positive integer.")


def encrypt(plaintext, key):
    """Arrange plaintext in a zigzag and read the rails from top to bottom."""
    validate_key(key)
    if not isinstance(plaintext, str):
        raise ValueError("Plaintext must be a string.")

    if key == 1 or key >= len(plaintext):
        return plaintext

    rails = [[] for _ in range(key)]
    row = 0
    direction = 1

    for character in plaintext:
        rails[row].append(character)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    ciphertext = ""
    for rail in rails:
        ciphertext += "".join(rail)

    return ciphertext


if __name__ == "__main__":
    try:
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the number of rails: "))
        print("Ciphertext:", encrypt(plaintext, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

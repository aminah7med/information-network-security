"""Rail Fence Cipher decryption."""

from rail_fence_encryption_supplementary import validate_key


def decrypt(ciphertext, key):
    """Rebuild the zigzag rails and read them in the original path."""
    validate_key(key)
    if not isinstance(ciphertext, str):
        raise ValueError("Ciphertext must be a string.")

    if key == 1 or key >= len(ciphertext):
        return ciphertext

    rail_counts = [0] * key
    rail_pattern = []
    row = 0
    direction = 1

    for _ in ciphertext:
        rail_pattern.append(row)
        rail_counts[row] += 1

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    # Split ciphertext into rails using the character counts from the pattern.
    rails = []
    start = 0
    for count in rail_counts:
        rails.append(list(ciphertext[start:start + count]))
        start += count

    # Follow the saved zigzag pattern, taking the next character from each rail.
    rail_positions = [0] * key
    plaintext = []
    for row in rail_pattern:
        plaintext.append(rails[row][rail_positions[row]])
        rail_positions[row] += 1

    return "".join(plaintext)


if __name__ == "__main__":
    try:
        ciphertext = input("Enter the ciphertext: ")
        key = int(input("Enter the number of rails: "))
        print("Plaintext:", decrypt(ciphertext, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

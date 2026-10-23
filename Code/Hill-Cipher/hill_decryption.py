"""Hill Cipher decryption using modular matrix inversion."""

from math import gcd

from hill_encryption import MODULUS, normalize_text, read_key_matrix, validate_key_matrix


def determinant(matrix):
    """Calculate a square matrix determinant by cofactor expansion."""
    dimension = len(matrix)
    if dimension == 1:
        return matrix[0][0]
    if dimension == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0
    for column, value in enumerate(matrix[0]):
        minor = [
            row[:column] + row[column + 1:]
            for row in matrix[1:]
        ]
        result += (-1) ** column * value * determinant(minor)

    return result


def modular_inverse(value, modulus):
    """Return the multiplicative inverse, rejecting values without one."""
    value %= modulus
    for candidate in range(modulus):
        if (value * candidate) % modulus == 1:
            return candidate

    raise ValueError(f"{value} has no multiplicative inverse modulo {modulus}.")


def inverse_key_matrix(key_matrix):
    """Calculate a square matrix inverse modulo 26."""
    dimension = validate_key_matrix(key_matrix)
    det = determinant(key_matrix)
    if gcd(det, MODULUS) != 1:
        raise ValueError(
            "Key matrix is not invertible modulo 26: "
            "its determinant must be coprime to 26."
        )

    determinant_inverse = modular_inverse(det, MODULUS)
    if dimension == 1:
        return [[determinant_inverse]]

    cofactors = []
    for row_index in range(dimension):
        cofactor_row = []
        for column_index in range(dimension):
            minor = [
                row[:column_index] + row[column_index + 1:]
                for index, row in enumerate(key_matrix)
                if index != row_index
            ]
            cofactor = (-1) ** (row_index + column_index) * determinant(minor)
            cofactor_row.append(cofactor)
        cofactors.append(cofactor_row)

    adjugate = [
        [cofactors[row][column] for row in range(dimension)]
        for column in range(dimension)
    ]
    return [
        [(determinant_inverse * value) % MODULUS for value in row]
        for row in adjugate
    ]


def decrypt(ciphertext, key_matrix):
    """Decrypt complete blocks, returning any X padding unchanged."""
    dimension = validate_key_matrix(key_matrix)
    ciphertext = normalize_text(ciphertext, "Ciphertext")
    if len(ciphertext) % dimension:
        raise ValueError(
            "Ciphertext length must be divisible by the key matrix dimension."
        )

    inverse_matrix = inverse_key_matrix(key_matrix)
    plaintext = []
    for start in range(0, len(ciphertext), dimension):
        block = [ord(letter) - ord("A") for letter in ciphertext[start:start + dimension]]
        for row in inverse_matrix:
            value = sum(key_value * letter for key_value, letter in zip(row, block))
            plaintext.append(chr((value % MODULUS) + ord("A")))

    return "".join(plaintext)


if __name__ == "__main__":
    try:
        message = input("Enter the ciphertext (English letters only): ")
        key = read_key_matrix()
        print("Plaintext:", decrypt(message, key))
    except ValueError as error:
        raise SystemExit(f"Error: {error}") from error

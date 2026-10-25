
# Playfair Cipher - Encryption

# Step 1: Get the keyword and plaintext
keyword = input("Enter your keyword: ").lower().replace("j", "i")
plaintext = input("Enter your plaintext: ").lower()


# Step 2: Define the alphabet (I and J share one cell)
alphabet = "abcdefghiklmnopqrstuvwxyz"


# Step 3: Build the matrix letters
matrix_letters = ""

# Add unique keyword letters first
for char in keyword:
    if char in alphabet and char not in matrix_letters:
        matrix_letters += char

# Add the remaining alphabet letters
for char in alphabet:
    if char not in matrix_letters:
        matrix_letters += char


# Step 4: Build the 5x5 matrix
matrix = []

for i in range(0, 25, 5):
    row = matrix_letters[i:i + 5]
    matrix.append(row)

# Display the matrix
print("\nPlayfair Matrix:")
for row in matrix:
    print(" ".join(row))


# Step 5: Find the position of a character
def find_position(matrix, char):
    # Treat J as I
    if char == "j":
        char = "i"

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# Step 6: Prepare the plaintext
# Keep English letters only and replace J with I
plaintext = "".join(
    char for char in plaintext if char in "abcdefghijklmnopqrstuvwxyz"
).replace("j", "i")

prepared_text = ""
i = 0

while i < len(plaintext):
    first = plaintext[i]

    # Add X if the pair contains repeated letters
    if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
        second = "x"
        i += 1

    # Add X if the last character has no pair
    elif i + 1 >= len(plaintext):
        second = "x"
        i += 1

    # Otherwise, take the next character
    else:
        second = plaintext[i + 1]
        i += 2

    prepared_text += first + second


# Step 7: Encrypt one pair
def encrypt_pair(matrix, first, second):
    row1, col1 = find_position(matrix, first)
    row2, col2 = find_position(matrix, second)

    # Rule 1: Same row - move right
    if row1 == row2:
        col1 = (col1 + 1) % 5
        col2 = (col2 + 1) % 5

    # Rule 2: Same column - move down
    elif col1 == col2:
        row1 = (row1 + 1) % 5
        row2 = (row2 + 1) % 5

    # Rule 3: Rectangle - swap columns
    else:
        col1, col2 = col2, col1

    return matrix[row1][col1] + matrix[row2][col2]


# Step 8: Encrypt the complete plaintext
ciphertext = ""

for i in range(0, len(prepared_text), 2):
    first = prepared_text[i]
    second = prepared_text[i + 1]

    ciphertext += encrypt_pair(matrix, first, second)


# Step 9: Display the results
print("\nOriginal plaintext:", plaintext)
print("Prepared plaintext:", prepared_text)
print("Ciphertext:", ciphertext)
